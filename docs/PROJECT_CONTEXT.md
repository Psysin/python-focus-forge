# FocusForge – Projekt-Kontext für Claude

> **Für neue Sessions:** Diese Datei lesen + `docs/Projekt_01_FocusForge_BLUEPRINT.md` lesen.
> Dann ist Claude vollständig im Bild.

---

## 👤 Benutzer-Präferenzen

- **Lernstil:** Schritt für Schritt – Philipp schreibt Code selbst, Claude erklärt und leitet an
- **Git-Befehle:** Immer mit kurzer Erklärung (1-2 Sätze) was der Befehl tut
- **Flags & Kurzbefehle:** Immer erklären (z.B. `-v` = verbose, `-m` = message) – bei jedem Auftreten wiederholen bis verinnerlicht
- **Sprache:** Deutsch
- **Screenshots einfügen:** `Alt+V` im Claude Code CLI
- **Setup-Dateien:** Okay vorab zu generieren als Grundgerüst/Beispiel

## 🧠 Lernregeln (für alle Projekte)

- **Viele Zwischenfragen stellen** – Wissen aktiv abfragen, nicht nur erklären
- **Wiederholung ist gewünscht** – Konzepte und Flags ruhig mehrfach erklären
- **Ausführliche Erklärungen** – Philipp ist Anfänger, lieber zu viel Kontext als zu wenig
- **Eigene Worte** – Philipp soll Konzepte in eigenen Worten erklären (Lernkontrolle)
- **Analogien nutzen** – Abstrakte Konzepte mit Alltagsbeispielen erklären
- **Fehler als Lernchance** – Fehler nicht einfach korrigieren, sondern erklären warum

## 🔁 Für zukünftige Projekte

- Diese Lernregeln und Präferenzen in neues Projekt übertragen
- PROJECT_CONTEXT.md des neuen Projekts mit diesen Regeln befüllen

## 🖥️ Technisches Setup

- **OS:** Windows (PC + Laptop)
- **IDE:** VS Code
- **Terminal:** Git Bash (Standard)
- **Claude starten:** `claude` in Git Bash im Projektverzeichnis
- **Konversation wiederfinden:** `/resume` im Claude Code CLI
- **venv aktivieren:** `.venv\Scripts\Activate.ps1`
- **Python Interpreter in VS Code:** `.venv\Scripts\python.exe` auswählen (Klick unten rechts in Statusleiste) – muss nach Neustart manchmal neu gesetzt werden!
- **App starten:** `python src/focus_forge/main.py` im Terminal (nicht Play-Button)
- **Paket installiert:** `pip install -e .` wurde ausgeführt – focus_forge ist systemweit in venv bekannt

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
| #4 | Zeitformatierung – Sekunden zu MM:SS | ✅ Fertig |
| #5 | Phasenwechsel-Logik | ✅ Fertig |
| #6 | Start/Pause-Button mit laufendem Countdown | ✅ Fertig |
| #7 | Reset-Button | ✅ Fertig |
| #8 | Automatischer Phasenwechsel bei 00:00 | ✅ Fertig |
| #9 | Session-Zähler | ✅ Fertig |
| #10 | Akustisches Signal beim Phasenwechsel | ✅ Fertig |
| #11 | Lange Pause nach 4 Fokus-Sessions | ✅ Fertig |

## 🎓 Was bisher gelernt wurde

- Git-Workflow: `git add` → `git commit -m "..."` → `git push`
- Staging Area: Zwischenstufe vor dem Commit
- Flags: `-v` = verbose, `-m` = message, `-u` = upstream, `-e` = editable
- Flet: `ft.Text`, `ft.Button` (ElevatedButton ist deprecated!), `ft.Column`, `ft.Row`
- `ft.run(main)` statt `ft.app(target=main)` (deprecated seit 0.80)
- `def main(page)` empfängt die Leinwand von Flet (erstellt sie nicht)
- `if __name__ == "__main__"` verhindert Auto-Start beim Import
- `//` Ganzzahldivision, `%` Modulo (Rest)
- f-Strings mit `:02` für führende Nullen
- pytest: Tests mit `def test_...()` und `assert`
- `pip install -e .` macht Paket systemweit in venv bekannt
- Konstanten (GROSSBUCHSTABEN): Single Source of Truth
- `return` vs `raise ValueError`: normal beenden vs. Fehler werfen
- `async`/`await`: Timer läuft ohne GUI einzufrieren
- `nonlocal`: Variable aus äußerem Scope nutzen und verändern
- `not is_running`: Boolean umschalten (True↔False)
- `page.run_task()`: Async-Funktion in Flet starten
- Import-Reihenfolge (isort): stdlib → third-party → own modules (mit Leerzeilen)
- `known-first-party` in pyproject.toml für Ruff/isort
- Einrückung in Python: ersetzt Klammern/Semikolons, zeigt Zugehörigkeit
- `IndentationError`: Einrückung stimmt nicht überein
- deprecated = veraltet – Warnung dass etwas bald entfernt wird
- Button-Text ändern: `ft.Text` als `content` im Button, dann `.value` ändern
- Timer-Loop Reihenfolge: erst zählen, dann schlafen → kein Delay
- Anzeige vs. Variable: `countdown.value` = was der Nutzer sieht, `time_remaining` = was der Timer intern berechnet – beide müssen beim Reset zurückgesetzt werden
- `x = x` ist eine sinnlose Zuweisung (Variable weist sich selbst zu, ändert nichts)
- `unused` Import-Warnung: Funktion importiert aber noch nicht verwendet – verschwindet sobald sie genutzt wird
- Mehrere Imports aus demselben Modul in einer Zeile mit Komma: `from module import a, b, c`
- `nonlocal` braucht man nur wenn man eine Variable aus der äußeren Funktion **verändern** will (nicht nur lesen)
- State-Variablen (laufende Werte wie Zähler) gehören in `main.py`, nicht in `timer.py` – `timer.py` nur für Logik/Konstanten
- `page.update()` sendet Änderungen an die Anzeige – aber nur was vorher als `.value` gesetzt wurde
- `=+1` ist ein Schreibfehler, gemeint ist `+=1` (erhöhen um 1)
- Session-Zähler zählt abgeschlossene Fokus-Phasen – erst nach der Phase, nicht beim Start
- `try/except`: Sicherheitsnetz – versuche etwas, und falls ein Fehler auftritt, mach stattdessen das
- `None`: kein Wert, "nichts" – nicht dasselbe wie `0`! Eigener spezieller Wert in Python
- `if sound is not None`: prüfen ob eine Variable überhaupt einen Wert hat bevor man sie nutzt
- `Path(__file__)`: gibt den Pfad zur aktuellen Datei zurück – `.parent` geht einen Ordner höher
- `pathlib` für Pfade nutzen statt hardcodierter Strings – funktioniert auf Windows und Mac
- Dunder (`__file__`, `__name__`): spezielle eingebaute Variablen mit doppeltem Unterstrich, von Python selbst gesetzt
- `ruff check . --fix`: Fehler automatisch beheben lassen (nur wenn `[*]` markiert)
- `pygame.mixer.init()`: Audio-Subsystem initialisieren – muss vor der Nutzung aufgerufen werden
- Type Hints: `(param: int)` = erwartet Int rein, `-> int` = gibt Int zurück – freiwillig, Python braucht sie nicht aber Werkzeuge und Lesbarkeit profitieren
- Lange Pause: `get_break_duration(session_count)` prüft via `% 4 == 0` ob lange Pause fällig – `session_count != 0` verhindert lange Pause beim allerersten Start

## 📝 Wichtige Entscheidungen

- Logik (`timer.py`) und UI (`main.py`) strikt getrennt
- Nur `timer.py` wird mit pytest getestet (keine GUI-Tests)
- CI (`ci.yml.disabled`) erst aktivieren wenn pytest & ruff sicher beherrscht werden
- `ft.Button` statt `ft.ElevatedButton` (deprecated in Flet 0.80+)
- Button-Label als separates `ft.Text` Objekt um Text zur Laufzeit zu ändern

## 💡 Learnings aus diesem Projekt (für zukünftige Projekte)

Diese Punkte beschreiben, was im Lernprozess gut funktioniert hat und was beim nächsten Projekt von Anfang an besser geplant werden sollte.

### Was gut funktioniert hat
- Konzepte in eigenen Worten erklären lassen (Lernkontrolle)
- Bugs selbst finden lassen statt sie direkt zu korrigieren
- Wissensfragen nach jedem abgeschlossenen Schritt

### Was verbessert werden sollte
- **Kleinere Schritte:** Aufgaben noch feiner aufteilen – lieber 5 Mini-Schritte als 1 großer
- **Mehr Erklärungen:** Philipp braucht mehr Kontext und Erklärung pro Schritt, auch wenn etwas "offensichtlich" wirkt
- **Tutor-Stil von Anfang an**: Beim nächsten Projekt die PROJECT_CONTEXT.md direkt mit diesen Regeln starten, nicht erst nachträglich ergänzen
- **Hints statt Antworten:** Bei Fehlern zuerst Hinweise geben (z.B. "Schau dir Zeile X an"), erst wenn Philipp nicht weiterkommt die Lösung zeigen
- **Wiederholungen einplanen:** Konzepte aus früheren Issues kurz wiederholen wenn sie erneut auftauchen (z.B. `nonlocal`, `page.update()`)

*Zuletzt aktualisiert: Nach Issue #11 + Tests – MVP vollständig, 12 Tests grün. Nächstes: pyinstaller für Windows/Mac App-Datei*
