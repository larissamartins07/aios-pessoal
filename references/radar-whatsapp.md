---
bike-method-phase: 1  # Phase 1 — Training wheels. Run manually first.
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk.
---

# Radar de respostas pendentes no WhatsApp

Prompt salvo para rodar no **Claude in Chrome**, com o WhatsApp Web aberto, no início de cada janela: **9h, 11h, 14h, 16h e 18h**. Escopo e porquê: `decisions/log.md`, entrada de 2026-10-09.

Autonomia **L1 (Sugerido)**: o Radar só lê e lista. Você decide o que cobrar e o que responder.

## Como usar

1. Abra o WhatsApp Web e ative o Claude in Chrome.
2. No chat da extensão, digite `/radar` (atalho salvo em Configurações > Atalhos). Sem o atalho, cole o prompt abaixo.
3. Anote o número de pendências com mais de 2 dias no registro do fim desta página. É o KPI.

**Se mudar o prompt aqui, atualize o atalho na extensão também.** A extensão não lê este arquivo.

## Loop de melhoria

1. Toda rodada termina com a seção "Para melhorar o Radar".
2. Se tiver algo útil, cole essa seção no Claude Code (ou só fale "adiciona X às pessoais").
3. O Claude Code atualiza o prompt aqui e anota no Registro (coluna Erros do Radar).
4. Você copia o prompt novo para o atalho `/radar`.

Junte as sugestões e atualize no máximo 1 vez por dia, para não ficar mexendo no atalho toda hora.

## Prompt

```
Você é o Radar de respostas pendentes da Larissa. Analise o WhatsApp Web aberto nesta aba.

PRIORITÁRIAS (leia PRIMEIRO, sempre, mesmo sem atividade recente)
- Grupo Olist Envios (implantação do novo sistema de envios: várias pendências abertas).
- Grupos internos da Mexidona: Prioridades, Administrativo, Financeiro, RH, e qualquer outro
  grupo interno da equipe Mexidona.
- Conversa com a Jessica Schroeder.
- Nessas, revise os últimos 14 dias, mensagem por mensagem, até o fim. Não pule nenhuma.

ESCOPO (as demais)
- Conversas de trabalho (individuais e grupos) com atividade nos últimos 7 dias.
- Ignore estas conversas pessoais: Carrinho dos noivos; #12 R1157, N145; Igor Regis;
  Família Matos e amigos; Frederico; Clínica Dermatológica HR. Ignore também qualquer outro
  grupo claramente de família ou amigos.
- Ignore sem abrir: canais, listas de transmissão e grupos automáticos ou de massa, como os que
  têm no nome "Abastecimento", "Grupo Vip Mexidona" ou o nome de uma rede/loja de supermercado
  (ex.: FESTVAL, MUFFATO, GIASSI).
- Ignore grupos em que a Larissa não escreveu nada nos últimos 7 dias.
- Depois desses filtros, leia TODAS as conversas que sobrarem. Se não der tempo, diga quantas
  ficaram sem ler.

O QUE PROCURAR
A) TE DEVEM: mensagens da Larissa que pedem algo (pergunta, pedido, cobrança, pedido de
   aprovação ou de número) e que ainda não tiveram resposta da pessoa a quem foram dirigidas.
   - Em grupos, a resposta precisa vir da pessoa citada ou de quem claramente ficou responsável.
   - Só sai da lista quando o pedido foi de fato resolvido (veio a resposta, o número, o arquivo,
     a aprovação). "ok", "👍", "vou ver" ou promessa ("finalizo hoje", "mando amanhã") NÃO resolvem:
     mantenha na lista e acrescente "(prometeu [quando])" ou "(só confirmou)".
   - Para cada item, diga em poucas palavras O QUE falta (não só o assunto da conversa).
B) VOCÊ DEVE: mensagens de outras pessoas que pedem algo à Larissa e que ela ainda não respondeu
   (nem com "ok").
- Percorra TODAS as mensagens dos últimos 7 dias de cada conversa, não só a mais recente:
  um pedido do começo da semana pode ter ficado para trás no meio de outras mensagens.
- Áudio que ficou sem resposta: liste como "áudio sem resposta" (não dá para saber o conteúdo).
- Mensagens encaminhadas e conversas entre outras pessoas não contam.
- Em grupos movimentados (ex.: Olist Envios), só entra o que a Larissa pediu ou o que pediram
  diretamente a ela. Dúvidas operacionais resolvidas entre a equipe não entram.
- Não reaproveite relatórios anteriores desta conversa: leia tudo de novo a cada rodada.

SAÍDA (só isto, curto)
## Te devem
| Quem | O que a Larissa pediu (até 12 palavras) | Desde | Dias | Conversa |
## Você deve
| Quem | O que pediram (até 12 palavras) | Desde | Dias | Conversa |

- Ordene da pendência mais antiga para a mais nova. Na coluna "Desde", use a data (DD/MM).
- Marque com ⚠️ o que tiver mais de 2 dias.
- Na coluna "O que", acrescente "→ tarefa?" quando for uma ação com prazo maior que 1 dia
  (deveria ir para a planilha do Pulso).
- Depois das tabelas: "Pendências com mais de 2 dias: N (te devem: X · você deve: Y)".

## Para melhorar o Radar (no máximo 3 itens; se não houver nada, escreva "nada")
- Conversa que parece pessoal e não está na lista de ignoradas: "Adicionar [nome] às pessoais?"
- Caso em que você ficou em dúvida se era pendência, e por quê.
- Ajuste no prompt que evitaria um erro desta rodada (uma frase).

REGRAS
- Leia só o TEXTO da página (leitura de texto ou da estrutura da página). Não tire capturas de tela
  nem dê zoom para conferir: isso gasta muito e não traz nada que o texto não tenha.
- NUNCA envie mensagem, reaja, apague, arquive ou fixe nada.
- Resuma; não copie valores financeiros, dados pessoais ou trechos longos.
- Se não conseguir ler uma conversa, diga qual e siga com as outras.
```

## Limitações conhecidas

- **Abrir uma conversa marca as mensagens como lidas** (ticks azuis). As pessoas podem achar que você leu. Na fase 1 isso é aceitável. Se incomodar, a gente ajusta o prompt para usar só a lista de conversas onde der.
- **O Claude in Chrome lê rolando a tela.** Conversas muito longas podem ter pendências antigas não vistas. Por isso o escopo é de 7 dias.
- **A classificação é estimativa da IA.** Confira os itens ⚠️ antes de cobrar alguém.

## Como evoluir (Bike Method)

| Fase | Quando avançar | O que muda |
|---|---|---|
| 1 (agora) | — | Prompt manual, só lista |
| 2 | Depois de cerca de 10 rodadas em 2 semanas, com no máximo 1 erro relevante por rodada | Radar rascunha a cobrança ou a resposta no seu tom (`references/voice.md`), para você copiar (L2) |
| 3 | Rascunhos aprovados quase sem edição por 2 semanas | Avaliar agente ou execução agendada, se o Claude in Chrome permitir, e integrar com o `/marca-passo` (pendência que é tarefa vira proposta na planilha) |

A fase só avança com edição explícita do `bike-method-phase` no topo deste arquivo.

## Registro (KPI)

Ponto de partida: tempo de tela do WhatsApp no celular = **1h52/dia** (semana até 09/10, sem contar o WhatsApp Web).

| Data | Janela | Pendências > 2 dias (te devem / você deve) | Erros do Radar | Observação |
|---|---|---|---|---|
| 09/10/2026 | 11h (rodado 12h) | 1 (1 / 0) | Olhou só a mensagem mais recente de cada conversa; não ouve áudios; histórico curto em conversas pouco ativas | 1ª rodada. 8 te devem, 3 você deve. Prompt ajustado depois desta rodada |
| 10/10/2026 | — (1ª com `/radar`) | 1 (1 / 0) | Não leu todas: +100 conversas, gastou tempo com grupos automáticos; itens vagos ("conversa sobre distribuição"); deixou passar 2 pendências no grupo Olist Envios | 5 te devem, 0 você deve. Ajustes: +2 pessoais, filtro de grupos automáticos, só sai da lista quando resolvido (ok e promessa não fecham), grupos prioritários com 14 dias |
| 10/10/2026 | — (2ª, prompt com prioritárias) | 2 (2 / 0) | Reaproveitou o relatório anterior nas conversas não prioritárias; não pegou o treinamento do CRM com o João; Luciane continua vaga | 13 te devem, 1 você deve. Achou as pendências do Olist Envios. Ajustes: regra para grupos movimentados, não reaproveitar relatório, data em "Desde" |
