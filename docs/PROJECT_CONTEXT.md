# FocusForge – Projekt-Kontext für Claude

## 👤 Benutzer-Präferenzen

- **Lernstil:** Schritt für Schritt, will selbst Code schreiben – Claude erklärt nur, generiert nicht alles vor
- **Git-Befehle:** Immer mit kurzer Erklärung (1-2 Sätze) was der Befehl tut
- **Sprache:** Deutsch
- **Setup-Dateien:** Okay vorab zu generieren (Grundgerüst zeigt wie es aussehen kann)

## 🖥️ Technisches Setup

- **OS:** Windows (PC + Laptop)
- **IDE:** VS Code
- **Terminal:** Git Bash (Standard)
- **Claude:** Claude Code CLI, Start mit `claude` in Git Bash
- **Conversation wiederfinden:** `/resume` im Claude Code CLI
- **venv aktivieren:** `.venv\Scripts\Activate.ps1` im Projektverzeichnis
- **Python Interpreter in VS Code:** `.venv\Scripts\python.exe` auswählen (Klick unten rechts in Statusleiste)

## 📁 Projekt: FocusForge

- **Beschreibung:** Pomodoro-Timer mit Flet GUI (Python Lernprojekt #1)
- **GitHub:** https://github.com/Psysin/python-focus-forge
- **Blueprint:** `docs/Projekt_01_FocusForge_BLUEPRINT.md`

## ✅ Issue-Status

| Issue | Titel | Status |
|-------|-------|--------|
| #1 | Projektstruktur und Entwicklungsumgebung | ✅ Fertig |
| #2 | Leeres Flet-Fenster mit App-Titel | ✅ Fertig |
| #3 | Timer-Layout mit statischer Anzeige | ✅ Fertig |
| #4 | Zeitformatierung – Sekunden zu MM:SS | 🔜 Nächstes |
| #5 | Phasenwechsel-Logik | ⏳ Ausstehend |
| #6 | Start/Pause-Button mit laufendem Countdown | ⏳ Ausstehend |
| #7 | Reset-Button | ⏳ Ausstehend |
| #8 | Automatischer Phasenwechsel bei 00:00 | ⏳ Ausstehend |
| #9 | Session-Zähler | ⏳ Ausstehend |

## 📝 Wichtige Entscheidungen

- Logik (`timer.py`) und UI (`main.py`) strikt getrennt
- Nur `timer.py` wird mit pytest getestet (keine GUI-Tests)
- CI (`ci.yml.disabled`) erst aktivieren, wenn pytest & ruff sicher beherrscht werden

## 🔄 Update-Anweisung

Bitte diese Datei nach jeder abgeschlossenen Session aktualisieren (Issue-Status, neue Entscheidungen).
