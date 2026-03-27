# FocusForge – Projekt-Kontext für Claude

> **Für neue Sessions:** Diese Datei lesen + `docs/Projekt_01_FocusForge_BLUEPRINT.md` lesen.
> Dann ist Claude vollständig im Bild.

---

## 👤 Benutzer-Präferenzen

- **Lernstil:** Schritt für Schritt – Philipp schreibt Code selbst, Claude erklärt und leitet an
- **Git-Befehle:** Immer mit kurzer Erklärung (1-2 Sätze) was der Befehl tut
- **Sprache:** Deutsch
- **Screenshots einfügen:** `Alt+V` im Claude Code CLI
- **Setup-Dateien:** Okay vorab zu generieren als Grundgerüst/Beispiel

## 🖥️ Technisches Setup

- **OS:** Windows (PC + Laptop)
- **IDE:** VS Code
- **Terminal:** Git Bash (Standard)
- **Claude starten:** `claude` in Git Bash im Projektverzeichnis
- **Konversation wiederfinden:** `/resume` im Claude Code CLI
- **venv aktivieren:** `.venv\Scripts\Activate.ps1`
- **Python Interpreter in VS Code:** `.venv\Scripts\python.exe` auswählen (Klick unten rechts in Statusleiste) – muss nach Neustart manchmal neu gesetzt werden!
- **App starten:** `python src/focus_forge/main.py` im Terminal (nicht Play-Button)

## 📁 Projekt

- **Beschreibung:** Pomodoro-Timer mit Flet GUI (Python Lernprojekt #1)
- **GitHub:** https://github.com/Psysin/python-focus-forge
- **Blueprint (alle Details):** `docs/Projekt_01_FocusForge_BLUEPRINT.md`

## ✅ Issue-Status

| Issue | Titel | Status |
|-------|-------|--------|
| #1 | Projektstruktur und Entwicklungsumgebung | ✅ Fertig |
| #2 | Leeres Flet-Fenster mit App-Titel | ✅ Fertig |
| #3 | Timer-Layout mit statischer Anzeige | ✅ Fertig |
| #4 | Zeitformatierung – Sekunden zu MM:SS | 🔄 In Arbeit |
| #5 | Phasenwechsel-Logik | ⏳ Ausstehend |
| #6 | Start/Pause-Button mit laufendem Countdown | ⏳ Ausstehend |
| #7 | Reset-Button | ⏳ Ausstehend |
| #8 | Automatischer Phasenwechsel bei 00:00 | ⏳ Ausstehend |
| #9 | Session-Zähler | ⏳ Ausstehend |

## 🎓 Was bisher gelernt wurde

- Git-Workflow: `git add` → `git commit -m "..."` → `git push`
- Staging Area: Zwischenstufe vor dem Commit
- Flet: `ft.Text` (Anzeige), `ft.ElevatedButton`, `ft.Column` (vertikal), `ft.Row` (horizontal)
- `def main(page)` empfängt die Leinwand von Flet (erstellt sie nicht)
- `if __name__ == "__main__"` verhindert Auto-Start beim Import

## 📝 Wichtige Entscheidungen

- Logik (`timer.py`) und UI (`main.py`) strikt getrennt
- Nur `timer.py` wird mit pytest getestet (keine GUI-Tests)
- CI (`ci.yml.disabled`) erst aktivieren wenn pytest & ruff sicher beherrscht werden

---
## 🔄 Aktuell in Arbeit

**Issue #4: `format_time()` in `timer.py`**
- ✅ Negativer Fall fertig: `if seconds < 0: return "00:00"`
- ❌ Noch fehlt: `minutes` (//), `secs` (%), `return f-String`
- Danach: Erste pytest-Tests in `tests/test_timer.py` schreiben

*Zuletzt aktualisiert: Während Issue #4*
