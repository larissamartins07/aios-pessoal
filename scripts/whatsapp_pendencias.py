"""Triagem de pendências do WhatsApp para o Radar.

Fonte padrão: o banco da ponte do WhatsApp MCP (C:\\Users\\Laris\\whatsapp-mcp\\whatsapp-bridge\\store\\messages.db),
aberto só para leitura. Não abre conversa no celular, então não marca nada como lido.
Com --exports, lê os exports "Sem mídia" (.zip ou .txt) de C:\\Users\\Laris\\.aios\\whatsapp\\.
Lista só os candidatos a pendência, com as mensagens que vieram depois, para o Claude decidir o que ficou
realmente em aberto. Não grava nada; só imprime.

Candidatos:
  TE DEVEM   mensagem da Larissa com pergunta ou pedido
  VOCÊ DEVE  mensagem de outra pessoa que cita a Larissa (ou pergunta, em conversa individual)
             e depois da qual a Larissa não escreveu mais nada

Filtros do banco (iguais aos do prompt do Radar): ignora canais, listas, conversas pessoais e grupos de massa;
grupo só entra se a Larissa escreveu nele nos últimos 7 dias, menos os prioritários (sempre entram).

Uso:
  python pessoal/scripts/whatsapp_pendencias.py [--dias 7] [--conversa trecho-do-nome]
  python pessoal/scripts/whatsapp_pendencias.py --exports [--pasta DIR]
"""

import argparse
import re
import sqlite3
import sys
import zipfile
from datetime import datetime, timedelta
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

PASTA = Path.home() / ".aios" / "whatsapp"
BANCO = Path.home() / "whatsapp-mcp" / "whatsapp-bridge" / "store" / "messages.db"
EU = "Larissa Leal"
MEU_NUMERO = "554898151718"  # conversa consigo mesma (bloco de notas) não entra
PRIORITARIAS = re.compile(r"olist envios|prioridades|administrativo|financeiro|\brh\b|mexidona|jessica", re.I)
PESSOAIS = re.compile(r"carrinho dos noivos|#12 r1157|igor regis|fam[ií]lia matos|frederico|cl[ií]nica dermatol|"
                      r"alessandra m warmling|grupo souza martins", re.I)
MASSA = re.compile(r"abastecimento|grupo vip mexidona|festval|muffato|giassi", re.I)
IGNORADAS = re.compile(r"86278091579606")  # trabalho, mas a Larissa pediu para ignorar (Agnes, transportadora MID)
MIDIA = {"audio": "áudio", "image": "imagem", "video": "vídeo", "document": "documento", "sticker": "figurinha"}
LINHA = re.compile(r"^\[(\d{2}/\d{2}/\d{4}), (\d{2}:\d{2}:\d{2})\] ([^:]+): (.*)$")
INVISIVEIS = dict.fromkeys(map(ord, "\u200e\u200f\u202a\u202c\u2068\u2069\ufeff"), None)
PEDIDO = re.compile(
    r"\?|\b(pode[mr]?|consegue[mr]?|preciso|precisamos|me (manda|envia|passa|avisa)|manda[r]?|envia[r]?|"
    r"verifica[r]?|confere|conferir|confirma[r]?|favor|aguardo|cad[eê]|retorno|providenciar|ver isso)\b", re.I)
CITA_EU = re.compile(r"@\s*Larissa|\bLari(ssa)?\b", re.I)
RUIDO = re.compile(r"^(áudio|imagem|vídeo|figurinha|documento|GIF) (ocultad|omitid)[oa]$|mensagem apagada|"
                   r"criptografia de ponta|adicionou|saiu$|removeu|mudou a imagem|criou o grupo", re.I)
FECHOU = re.compile(r"obrigad|perfeito|show|[óo]timo|beleza|valeu|combinado|resolvid|top|👍|🙏|🧡|❤", re.I)
CORTE, CORTE_RESP, MAX_RESP = 200, 90, 4
JANELA = 12  # mensagens seguintes olhadas para decidir se houve resposta ou fechamento


def ler(arquivo):
    if arquivo.suffix == ".zip":
        with zipfile.ZipFile(arquivo) as z:
            nome = next((n for n in z.namelist() if n.endswith(".txt")), None)
            return z.read(nome).decode("utf-8", "replace") if nome else ""
    return arquivo.read_text(encoding="utf-8", errors="replace")


def mensagens(texto):
    msgs = []
    for bruta in texto.splitlines():
        linha = bruta.translate(INVISIVEIS)
        m = LINHA.match(linha)
        if m:
            quando = datetime.strptime(f"{m[1]} {m[2]}", "%d/%m/%Y %H:%M:%S")
            msgs.append({"quando": quando, "quem": m[3].lstrip("~ ").strip(), "texto": m[4].strip()})
        elif msgs and linha.strip():
            msgs[-1]["texto"] += " / " + linha.strip()
    return [m for m in msgs if not RUIDO.search(m["texto"])]


def do_banco(desde, filtro):
    """Conversas do banco da ponte no formato de mensagens(), já filtradas como no prompt do Radar."""
    con = sqlite3.connect(f"file:{BANCO}?mode=ro", uri=True)
    nomes = {jid.split("@")[0]: nome for jid, nome in con.execute("select jid, name from chats") if nome}
    recente = datetime.now() - timedelta(days=7)
    conversas = []
    for jid, nome in con.execute("select jid, coalesce(name, jid) from chats order by last_message_time desc"):
        if jid.endswith(("@newsletter", "@broadcast")) or jid.startswith(MEU_NUMERO) or PESSOAIS.search(nome) \
                or MASSA.search(nome) or IGNORADAS.search(jid):
            continue
        if filtro.lower() not in nome.lower():
            continue
        linhas = con.execute("select sender, content, timestamp, is_from_me, media_type from messages "
                             "where chat_jid = ? order by timestamp", (jid,)).fetchall()
        msgs = []
        for sender, texto, quando, meu, midia in linhas:
            quando = datetime.fromisoformat(quando).replace(tzinfo=None)
            texto = (texto or "").strip() or (f"{MIDIA.get(midia, midia)} (sem texto)" if midia else "")
            if texto:
                msgs.append({"quando": quando, "quem": EU if meu else nomes.get(sender, sender), "texto": texto})
        if not msgs or msgs[-1]["quando"] < desde:
            continue
        if jid.endswith("@g.us") and not PRIORITARIAS.search(nome) and \
                not any(m["quem"] == EU and m["quando"] >= recente for m in msgs):
            continue
        conversas.append((nome, msgs))
    return conversas


def curto(s, n):
    return s if len(s) <= n else s[: n - 1] + "…"


def agrupar(msgs):
    """Junta mensagens seguidas da mesma pessoa em menos de 5 min (um pedido costuma vir picado)."""
    out = []
    for m in msgs:
        if out and out[-1]["quem"] == m["quem"] and m["quando"] - out[-1]["fim"] < timedelta(minutes=5):
            out[-1]["texto"] += " / " + m["texto"]
            out[-1]["fim"] = m["quando"]
        else:
            out.append(dict(m, fim=m["quando"]))
    return out


def triar(nome, msgs, desde):
    msgs = agrupar(msgs)
    individual = len({m["quem"] for m in msgs} - {EU}) <= 1
    saida = []
    for i, m in enumerate(msgs):
        if m["quando"] < desde:
            continue
        seguintes = msgs[i + 1: i + 1 + JANELA]
        minhas = [d for d in seguintes if d["quem"] == EU]
        if m["quem"] == EU:
            if not PEDIDO.search(m["texto"]):
                continue
            outros = [d for d in seguintes if d["quem"] != EU]
            # alguém respondeu e a Larissa agradeceu/fechou depois: resolvido
            if outros and any(FECHOU.search(d["texto"]) for d in minhas if d["quando"] > outros[0]["quando"]):
                continue
            tipo, resp = "TE DEVEM", outros[:MAX_RESP]
        else:
            if not (CITA_EU.search(m["texto"]) or (individual and "?" in m["texto"])):
                continue
            if minhas:
                continue  # a Larissa escreveu logo depois: provavelmente respondeu
            tipo, resp = "VOCÊ DEVE", seguintes[:MAX_RESP]
        saida.append(f"- [{tipo}] {m['quando']:%d/%m %H:%M} {m['quem']}: {curto(m['texto'], CORTE)}")
        saida += [f"    > {d['quando']:%d/%m %H:%M} {d['quem']}: {curto(d['texto'], CORTE_RESP)}" for d in resp]
        if not resp:
            saida.append("    > (nada depois)")
    if saida:
        print(f"\n## {nome}\n" + "\n".join(saida))
    return sum(1 for s in saida if s.startswith("- ["))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=7)
    ap.add_argument("--exports", action="store_true", help="ler os exports em vez do banco da ponte")
    ap.add_argument("--pasta", type=Path, default=PASTA)
    ap.add_argument("--conversa", default="")
    a = ap.parse_args()
    desde = datetime.now() - timedelta(days=a.dias)
    if a.exports:
        arquivos = sorted(p for p in a.pasta.glob("*") if p.suffix in (".zip", ".txt"))
        conversas = [(arq.stem.replace("WhatsApp Chat - ", "").strip(), arq) for arq in arquivos]
        conversas = [(n, mensagens(ler(arq))) for n, arq in conversas if a.conversa.lower() in n.lower()]
    else:
        conversas = do_banco(desde, a.conversa)
        ultima = max((m["quando"] for _, ms in conversas for m in ms), default=None)
        print(f"Banco da ponte. Mensagem mais recente: {ultima:%d/%m %H:%M}" if ultima else "Banco da ponte vazio.")
    total = sum(triar(nome, msgs, desde) for nome, msgs in conversas)
    print(f"\nCandidatos: {total} em {len(conversas)} conversa(s), últimos {a.dias} dias.")


if __name__ == "__main__":
    main()
