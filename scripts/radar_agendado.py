"""Radar do WhatsApp nos horários (Agendador do Windows: dias úteis, 9h, 11h, 14h, 16h e 18h).

Roda whatsapp_pendencias.py no banco da ponte, salva os candidatos em C:\\Users\\Laris\\.aios\\whatsapp\\radar\\
(fora do OneDrive, tem dados de terceiros) e mostra um aviso no Windows. Quem decide o que é pendência é o Claude:
abrir o Claude Code e pedir "roda o radar" (pessoal/references/radar-whatsapp.md).
Se a ponte estiver fechada, avisa para abrir em vez de rodar.

Uso: pythonw pessoal/scripts/radar_agendado.py
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SAIDA = Path.home() / ".aios" / "whatsapp" / "radar"
PONTE = Path.home() / "whatsapp-mcp" / "whatsapp-bridge" / "whatsapp-bridge.exe"
PY = Path(sys.executable).with_name("python.exe")
SEM_JANELA = 0x08000000


def avisar(titulo, texto):
    esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("'", "&apos;")
    ps = f"""
[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
[Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime] | Out-Null
$x = New-Object Windows.Data.Xml.Dom.XmlDocument
$x.LoadXml('<toast scenario="reminder"><visual><binding template="ToastGeneric"><text>{esc(titulo)}</text><text>{esc(texto)}</text></binding></visual><actions><action content="Ok" arguments="ok" activationType="system"/></actions></toast>')
$t = [Windows.UI.Notifications.ToastNotification]::new($x)
[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('{{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}}\\WindowsPowerShell\\v1.0\\powershell.exe').Show($t)
"""
    subprocess.run(["powershell", "-NoProfile", "-Command", ps], creationflags=SEM_JANELA)


def ponte_aberta():
    r = subprocess.run(["tasklist", "/FI", "IMAGENAME eq whatsapp-bridge.exe", "/NH"], capture_output=True,
                       text=True, creationflags=SEM_JANELA)
    return "whatsapp-bridge.exe" in r.stdout


def main():
    if not ponte_aberta():
        avisar("Radar do WhatsApp", f"A ponte está fechada. Abra {PONTE} e depois peça \"roda o radar\" no Claude.")
        return
    r = subprocess.run([str(PY), "-X", "utf8", str(AQUI / "whatsapp_pendencias.py")], capture_output=True,
                       text=True, encoding="utf-8", creationflags=SEM_JANELA)
    SAIDA.mkdir(parents=True, exist_ok=True)
    arq = SAIDA / f"{datetime.now():%Y-%m-%d-%Hh%M}.txt"
    arq.write_text(r.stdout + (f"\n[erro]\n{r.stderr}" if r.returncode else ""), encoding="utf-8")
    if r.returncode:
        avisar("Radar do WhatsApp", "O script deu erro. Peça \"olha o radar\" no Claude.")
        return
    total = next((l.split()[1] for l in r.stdout.splitlines() if l.startswith("Candidatos:")), "?")
    avisar("Radar do WhatsApp", f"{total} candidatos a pendência. Abra o Claude e peça \"roda o radar\".")


if __name__ == "__main__":
    main()
