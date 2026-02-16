# 🔨 P01 – FocusForge: BLUEPRINT

> **Repo:** `python-focus-forge`
> **Typ:** 🖥️ Software (Flet GUI)
> **Phase:** 1 – Python-Grundlagen
> **Aufwand:** ⭐ (1/5)

---

## 1) Elevator Pitch

Ein Pomodoro-Timer mit Flet-GUI – starte 25-Minuten-Fokus-Sessions, mach 5 Minuten Pause, und behalte den Überblick über deine Produktivität. Dein allerstes „echtes" Python-Programm mit grafischer Oberfläche, professionellem Workflow und echten Tests.

---

## 2) Zielgruppe & Use-Case

**Typischer Nutzer:** Du selbst – als tägliches Produktivitäts-Tool und als erstes Lernprojekt.

**Szenario 1:** Du setzt dich an den Rechner zum Lernen, startest FocusForge, drückst „Start" und arbeitest fokussiert 25 Minuten. Die App erinnert dich automatisch an die Pause.

**Szenario 2:** Nach 4 Fokus-Sessions schaust du auf den Session-Zähler und siehst: „4 Sessions geschafft" – das motiviert dich, morgen genauso weiterzumachen.

---

## 3) MVP + Nice-to-have

### MVP (Must-have)

- Timer starten, pausieren und zurücksetzen
- Countdown-Anzeige im Format MM:SS
- Automatischer Phasenwechsel: Fokus (25 min) → Pause (5 min) → Fokus …
- Phasen-Anzeige: „FOKUS" oder „PAUSE" (mit unterschiedlicher Farbe)
- Session-Zähler: Anzahl abgeschlossener Fokus-Runden
- Start/Pause-Button (ein Button, Text wechselt) + Reset-Button
- Sauberes, zentriertes Layout

### Nice-to-have – Should

- Akustisches Signal beim Phasenwechsel
- Lange Pause (15 min) nach 4 Fokus-Sessions

### Nice-to-have – Could

- Konfigurierbare Zeiten (Fokus: 15/25/50, Pause: 5/10/15)
- Tages-Statistik: „Heute X Sessions, Y Minuten Fokus"
- Dark/Light Mode Toggle
- Keyboard-Shortcut: Leertaste = Start/Pause

---

## 4) Akzeptanzkriterien

- ✅ Wenn die App gestartet wird, dann öffnet sich ein Fenster mit Titel „FocusForge" und einer Countdown-Anzeige bei 25:00.
- ✅ Wenn der Start-Button geklickt wird, dann zählt der Timer jede Sekunde herunter (25:00 → 24:59 → …).
- ✅ Wenn der Timer läuft und der Pause-Button geklickt wird, dann stoppt der Countdown und kann fortgesetzt werden.
- ✅ Wenn der Reset-Button geklickt wird, dann springt der Timer auf den Startwert der aktuellen Phase zurück und stoppt.
- ✅ Wenn der Countdown 00:00 erreicht, dann wechselt die Phase automatisch (Fokus → Pause oder Pause → Fokus) und der neue Countdown startet.
- ✅ Wenn eine Fokus-Phase abgeschlossen wird, dann erhöht sich der Session-Zähler um 1.
- ✅ Wenn eine Pause-Phase abgeschlossen wird, dann bleibt der Session-Zähler unverändert.
- ✅ Wenn `pytest -v` ausgeführt wird, dann sind alle Tests grün.
- ✅ Wenn `ruff check .` ausgeführt wird, dann werden keine Fehler gemeldet.

---

## 5) UX-Skizze in Worten

### Einzige View: Timer-Hauptansicht

```
┌──────────────────────────────────┐
│          FocusForge 🔨           │  ← App-Titel, zentriert
│                                  │
│            FOKUS                 │  ← Phasen-Label (blau=Fokus, grün=Pause)
│                                  │
│           24:37                  │  ← Countdown, große Schrift, zentriert
│                                  │
│    [ ▶ Start ]   [ ↺ Reset ]    │  ← Buttons nebeneinander, zentriert
│                                  │
│      Sessions heute: 3           │  ← Zähler, kleine Schrift, unten
│                                  │
└──────────────────────────────────┘
```

**Navigation:** Keine – alles auf einem einzigen Bildschirm. Kein Routing, keine Tabs.

**Verhalten der Elemente:**

- **Start/Pause-Button:** Zeigt „▶ Start" im Ruhezustand. Wird zu „⏸ Pause" wenn Timer läuft. Gleicher Button, Text wechselt.
- **Reset-Button:** Immer sichtbar. Setzt Timer auf Phasen-Startwert zurück, stoppt ihn.
- **Phasen-Label:** Wechselt Text und Farbe bei Phasenwechsel.
- **Countdown:** Größte Schrift im Fenster. Aktualisiert sich jede Sekunde.
- **Session-Zähler:** Dezent unten, zählt nur abgeschlossene Fokus-Phasen.

**Responsive:** Flet skaliert automatisch. Standard-Fenstergröße ca. 400 × 450 px. Keine speziellen Mobile-/Desktop-Unterschiede nötig, da nur eine einzige vertikale Spalte.

---

## 6) Datenmodell

### Entities (Laufzeit-Variablen, keine Datenbank)

Für das MVP gibt es **keine Persistenz** – alle Daten leben im Arbeitsspeicher.

| Entity/Variable | Typ | Beschreibung | Startwert |
|-----------------|-----|-------------|-----------|
| `current_phase` | `str` | Aktive Phase | `"focus"` |
| `time_remaining_seconds` | `int` | Verbleibende Sekunden | `1500` |
| `is_running` | `bool` | Läuft der Timer? | `False` |
| `sessions_completed` | `int` | Abgeschlossene Fokus-Runden | `0` |

### Konstanten

| Konstante | Typ | Wert | Beschreibung |
|-----------|-----|------|-------------|
| `FOCUS_DURATION_SEC` | `int` | `1500` | 25 Minuten in Sekunden |
| `BREAK_DURATION_SEC` | `int` | `300` | 5 Minuten in Sekunden |
| `LONG_BREAK_DURATION_SEC` | `int` | `900` | 15 Minuten (Should) |
| `SESSIONS_BEFORE_LONG_BREAK` | `int` | `4` | Nach 4 Sessions: lange Pause (Should) |

### Beziehungen

Keine. Flaches Datenmodell. Keine 1:n oder n:m-Beziehungen.

**Persistenz-Entscheidung:** Keine Datei, keine Datenbank im MVP. Alle Werte leben nur während die App läuft. Für das Could-Feature „Tages-Statistik" wäre eine JSON-Datei denkbar – das ist aber explizit kein MVP-Scope.

---

## 7) Architektur

### Ordnerstruktur

```
python-focus-forge/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── feature_request.md
│   │   └── bug_report.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── ci.yml.disabled          ← CI-Vorlage, noch nicht aktiv
├── src/
│   └── focus_forge/
│       ├── __init__.py
│       ├── main.py                  ← app/ – UI: Flet-App aufbauen, Events binden
│       └── timer.py                 ← core/ – Logik: reine Funktionen, kein GUI-Bezug
├── tests/
│   ├── __init__.py
│   └── test_timer.py               ← Tests für die gesamte Timer-Logik
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── pyproject.toml                   ← ruff-/pytest-Konfiguration
└── requirements.txt
```

### Verantwortlichkeiten

| Bereich | Datei(en) | Verantwortung |
|---------|-----------|---------------|
| **app** (UI) | `main.py` | Flet-App initialisieren, UI-Elemente erstellen, Button-Events an Logik-Funktionen binden, Anzeige aktualisieren |
| **core** (Logik) | `timer.py` | Reine Funktionen: Sekunden → „MM:SS" formatieren, Phasenwechsel berechnen, Phasen-Dauer bestimmen. **Weiß nichts von Flet.** |
| **tests** | `test_timer.py` | Unit-Tests für jede Funktion in `timer.py`. Kein GUI-Test. |

**Kernprinzip:** Logik und UI sind getrennt. `timer.py` ist unabhängig testbar. `main.py` ruft `timer.py`-Funktionen auf, hat aber selbst keine berechenbare Logik.

---

## 8) Tech-Entscheidungen

| Bereich | Wahl | Begründung |
|---------|------|-----------|
| **UI** | **Flet** | Python-only, kein HTML/CSS nötig. Desktop + Web + Mobile aus einer Codebasis. Ideal als erstes GUI-Framework. |
| **Timer-Mechanismus** | Flet-internes `page.run_task()` mit `asyncio.sleep()` | Vermeidet Threading-Komplexität. Flet unterstützt async nativ – einfachster Weg für einen Anfänger. |
| **Persistenz** | **Keine** (MVP) | Ein Timer braucht keine Datenbank. Alles im RAM. Dateien/SQLite kommen in späteren Projekten. |
| **Linter/Formatter** | **ruff** | Projektstandard laut ROADMAP_MASTER. Extrem schnell, ersetzt flake8+black+isort. |
| **Tests** | **pytest** | Projektstandard. Nur `timer.py` wird getestet (reine Logik). Kein GUI-Testing für Anfänger. |
| **CI** | **Deaktiviert** (ci.yml.disabled) | Erstes Projekt. CI-Datei liegt als Referenz im Repo, wird aber erst aktiviert wenn Philipp pytest und ruff lokal sicher beherrscht. |

---

## 9) Backlog als Issues

> Gliederung: **Setup → UI-Grundgerüst → Logik → Features → Polish → Release**

---

### 🔧 Phase A: Setup

#### Issue #1: `chore: Projektstruktur und Entwicklungsumgebung anlegen`

**Beschreibung:** Repo auf GitHub erstellen, lokal klonen, Ordnerstruktur nach ROADMAP_MASTER anlegen, venv einrichten, Abhängigkeiten installieren, GitHub-Templates einrichten.

**Akzeptanzkriterien:**
- [ ] Repo `python-focus-forge` existiert auf GitHub (Public, MIT-Lizenz, Python-.gitignore)
- [ ] Ordnerstruktur wie in Abschnitt 7 ist vollständig angelegt
- [ ] `requirements.txt` enthält `flet`, `pytest`, `ruff`
- [ ] `pyproject.toml` enthält ruff- und pytest-Konfiguration
- [ ] `python -c "import flet"` funktioniert in der aktivierten venv

**Tests:** Keine (Infrastruktur-Issue).

**DoD:**
- PR gemergt in `main`
- `pip install -r requirements.txt` in frischer venv funktioniert
- ruff/format läuft ohne Fehler auf dem leeren Projekt
- `.github/`-Templates liegen im Repo

**VS Code Hinweis:**
- Terminal öffnen: `Ctrl+Shift+Ö`
- venv erstellen: `python -m venv .venv`
- venv aktivieren: `.venv\Scripts\Activate.ps1`
- Interpreter auswählen: `Ctrl+Shift+P` → „Python: Select Interpreter" → `.venv` wählen
- Wenn PowerShell sich über ExecutionPolicy beschwert: einmalig `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` als Admin ausführen

---

### 🖼️ Phase B: UI-Grundgerüst

#### Issue #2: `feat: Leeres Flet-Fenster mit App-Titel starten`

**Beschreibung:** `main.py` startet eine minimale Flet-App: Fenster öffnet sich, zeigt den Titel „FocusForge", sonst nichts. Beweis, dass Flet funktioniert.

**Akzeptanzkriterien:**
- [ ] `python src/focus_forge/main.py` öffnet ein Fenster
- [ ] Fenstertitel ist „FocusForge"
- [ ] Fenstergröße ca. 400 × 450 px
- [ ] X-Button schließt die App sauber (kein Prozess hängt)

**Tests:** Manueller Smoke-Test: „Geht das Fenster auf und lässt es sich schließen?"

**DoD:**
- Code in `main.py` fertig
- Manuell getestet: Fenster öffnet, schließt
- ruff sauber
- PR gemergt

**VS Code Hinweis:**
- Datei ausführen: Terminal → `python src/focus_forge/main.py`
- Alternativ: Datei öffnen → `Ctrl+F5` (Run without Debugging)
- Wenn das Fenster nicht aufgeht: Console-Output im Terminal lesen – Flet gibt klare Fehlermeldungen

---

#### Issue #3: `feat: Timer-Layout mit statischer Anzeige aufbauen`

**Beschreibung:** Das vollständige UI-Layout steht: Phasen-Label „FOKUS", Countdown „25:00", zwei Buttons (Start + Reset), Session-Zähler „Sessions heute: 0". Noch keine Funktionalität – nur das Layout.

**Akzeptanzkriterien:**
- [ ] „FOKUS" als Phasen-Label sichtbar (Akzentfarbe)
- [ ] „25:00" als großer Countdown-Text zentriert
- [ ] „▶ Start"-Button und „↺ Reset"-Button nebeneinander
- [ ] „Sessions heute: 0" am unteren Rand
- [ ] Alle Elemente vertikal zentriert im Fenster

**Tests:** Manuell: Visueller Abgleich mit der UX-Skizze aus Abschnitt 5.

**DoD:**
- Layout in `main.py` fertig
- Visuell geprüft
- ruff sauber
- PR gemergt

**VS Code Hinweis:**
- Flet-Dokumentation parallel im Browser öffnen (flet.dev/docs)
- Änderung speichern → App neu starten → Layout prüfen. (Hot-Reload kommt in späteren Projekten.)

---

### ⚙️ Phase C: Logik (testbar, ohne GUI)

#### Issue #4: `feat: Zeitformatierung – Sekunden zu MM:SS`

**Beschreibung:** In `timer.py` eine Funktion `format_time(seconds)` implementieren, die eine Ganzzahl in den String „MM:SS" umwandelt. Reine Logik, kein GUI.

**Akzeptanzkriterien:**
- [ ] `format_time(1500)` → `"25:00"`
- [ ] `format_time(90)` → `"01:30"`
- [ ] `format_time(0)` → `"00:00"`
- [ ] `format_time(3599)` → `"59:59"`
- [ ] Negative Werte werden als `"00:00"` behandelt

**Tests:**
- `test_format_time_full_minutes` → 1500 → "25:00"
- `test_format_time_mixed` → 90 → "01:30"
- `test_format_time_zero` → 0 → "00:00"
- `test_format_time_large` → 3599 → "59:59"
- `test_format_time_negative` → -5 → "00:00"

**DoD:**
- Funktion in `timer.py` fertig
- 5 Tests in `test_timer.py` grün
- ruff sauber
- PR gemergt

**VS Code Hinweis:**
- Hier schreibst du deine **allerersten pytest-Tests!**
- Tests ausführen: Terminal → `pytest -v`
- Test Explorer: Klick auf 🧪 in der linken Leiste → Tests als Baum sehen → einzeln oder alle ausführen
- Wenn Tests rot sind: Fehlermeldung lesen – pytest zeigt dir genau, was erwartet wurde vs. was kam

---

#### Issue #5: `feat: Phasenwechsel-Logik`

**Beschreibung:** Zwei Funktionen in `timer.py`: `get_next_phase(current_phase)` gibt die nächste Phase zurück, `get_phase_duration(phase)` gibt die Dauer in Sekunden zurück.

**Akzeptanzkriterien:**
- [ ] `get_next_phase("focus")` → `"break"`
- [ ] `get_next_phase("break")` → `"focus"`
- [ ] `get_phase_duration("focus")` → `1500`
- [ ] `get_phase_duration("break")` → `300`

**Tests:**
- `test_next_phase_focus_to_break`
- `test_next_phase_break_to_focus`
- `test_duration_focus` → 1500
- `test_duration_break` → 300

**DoD:**
- 2 Funktionen in `timer.py` fertig
- 4 neue Tests grün (Gesamt jetzt: 9)
- ruff sauber
- PR gemergt

**VS Code Hinweis:**
- `pytest -v -k "next_phase"` filtert nur Phasenwechsel-Tests → nützlich wenn du an einem Teilbereich arbeitest
- Breakpoint in `get_next_phase` setzen und mit F5 debuggen: Siehst du den Parameter `current_phase` im Variables-Panel?

---

### 🎯 Phase D: Features (GUI + Logik verknüpfen)

#### Issue #6: `feat: Start/Pause-Button mit laufendem Countdown`

**Beschreibung:** Der Start-Button startet den Countdown (25:00 → 24:59 → …). Button-Text wechselt zu „⏸ Pause". Erneuter Klick pausiert, Weiterer Klick setzt fort.

**Akzeptanzkriterien:**
- [ ] Klick auf „▶ Start" → Countdown läuft, Button zeigt „⏸ Pause"
- [ ] Klick auf „⏸ Pause" → Countdown stoppt, Button zeigt „▶ Start"
- [ ] Fortsetzen startet ab dem pausierten Wert (nicht von vorne)
- [ ] Countdown aktualisiert die Anzeige jede Sekunde

**Tests:**
- Logik-Tests aus Issue #4 und #5 decken die Berechnung ab
- Manuell: Timer starten → pausieren → fortsetzen → Zeiten stimmen?

**DoD:**
- Timer-Steuerung in `main.py` funktioniert
- Manuell getestet
- ruff sauber
- PR gemergt

**VS Code Hinweis:**
- Hier nutzt du `async`/`await` zum ersten Mal (Flet's `page.run_task()`)
- Wenn das GUI einfriert: Du hast vermutlich `time.sleep()` im Haupt-Thread benutzt → stattdessen `await asyncio.sleep(1)` innerhalb einer async-Funktion

---

#### Issue #7: `feat: Reset-Button`

**Beschreibung:** Der Reset-Button setzt den Timer auf den Startwert der aktuellen Phase zurück und stoppt ihn.

**Akzeptanzkriterien:**
- [ ] Klick setzt `time_remaining_seconds` auf die Dauer der aktuellen Phase
- [ ] Timer stoppt (falls er lief)
- [ ] Anzeige aktualisiert sich sofort (z.B. zurück auf „25:00")
- [ ] Start-Button zeigt wieder „▶ Start"
- [ ] Session-Zähler wird NICHT zurückgesetzt

**Tests:** Manuell: Timer starten → warten → Reset → zeigt 25:00 → Sessions-Zähler unverändert.

**DoD:**
- Reset-Logik in `main.py` fertig
- Manuell in verschiedenen Zuständen getestet (laufend, pausiert, nach Phasenwechsel)
- ruff sauber
- PR gemergt

**VS Code Hinweis:**
- Teste den Reset in drei Situationen: (1) Timer läuft, (2) Timer pausiert, (3) Timer gerade bei 00:00 angekommen. Alle drei müssen sauber funktionieren.

---

#### Issue #8: `feat: Automatischer Phasenwechsel bei 00:00`

**Beschreibung:** Wenn der Countdown 00:00 erreicht, wechselt die App automatisch in die nächste Phase und startet den neuen Timer.

**Akzeptanzkriterien:**
- [ ] Bei 00:00 wechselt die Phase automatisch (Fokus → Pause / Pause → Fokus)
- [ ] Phasen-Label aktualisiert Text und Farbe
- [ ] Neuer Countdown startet automatisch mit der richtigen Dauer
- [ ] Kein manueller Klick nötig für den Wechsel

**Tests:**
- Phasenwechsel-Logik ist in Issue #5 getestet
- Manuell: Timer mit **kurzer Test-Dauer** testen (z.B. 5 Sekunden statt 25 Minuten), um den Wechsel schnell zu sehen

**DoD:**
- Phasenwechsel in `main.py` integriert
- Manuell getestet (mit verkürzter Dauer)
- ruff sauber
- PR gemergt

**VS Code Hinweis:**
- Tipp zum Testen: Temporär `FOCUS_DURATION_SEC = 5` setzen, damit du nicht 25 Minuten warten musst. **Vor dem Commit zurücksetzen!**

---

#### Issue #9: `feat: Session-Zähler`

**Beschreibung:** Nach jeder abgeschlossenen Fokus-Phase erhöht sich der Session-Zähler um 1. Anzeige: „Sessions heute: X" unten im Fenster.

**Akzeptanzkriterien:**
- [ ] Beim Start zeigt der Zähler „Sessions heute: 0"
- [ ] Nach einer vollständigen Fokus-Phase: Zähler wird 1
- [ ] Abschluss einer Pause erhöht den Zähler NICHT
- [ ] Reset setzt den Zähler NICHT zurück

**Tests:**
- `test_increment_sessions_after_focus` → von 0 auf 1
- `test_no_increment_after_break` → bleibt bei 1

**DoD:**
- Zähler-Logik als Funktion in `timer.py` (testbar)
- 2 neue Tests grün (Gesamt: 11)
- UI-Integration in `main.py`
- ruff sauber
- PR gemergt

**VS Code Hinweis:**
- Die Zähler-Logik gehört in `timer.py`, nicht in `main.py` – damit sie testbar bleibt. `main.py` ruft die Funktion nur auf.

---

### ✨ Phase E: Polish & Should-Features

#### Issue #10: `feat: Akustisches Signal bei Phasenwechsel`

**Beschreibung:** Beim Wechsel von Fokus → Pause und Pause → Fokus ertönt ein kurzer Sound.

**Akzeptanzkriterien:**
- [ ] Bei jedem Phasenwechsel ertönt ein Sound
- [ ] Sound ist kurz (< 2 Sekunden)
- [ ] Wenn kein Audio-Gerät vorhanden ist, crasht die App NICHT

**Tests:**
- Manuell: Phasenwechsel auslösen → Sound hörbar?
- Fehlerfall manuell prüfen: Sound-Datei umbenennen → App crasht nicht?

**DoD:**
- Sound-Integration fertig
- Fehlerfall abgefangen (try/except)
- ruff sauber
- PR gemergt

**VS Code Hinweis:**
- Sound-Datei (z.B. `.wav`) kommt in einen `assets/`-Ordner. Flet hat ein `Audio`-Control – in der Flet-Doku nachschlagen.

---

#### Issue #11: `feat: Lange Pause nach 4 Sessions`

**Beschreibung:** Nach 4 abgeschlossenen Fokus-Sessions wird die Pause 15 Minuten statt 5 Minuten. Danach beginnt ein neuer 4er-Zyklus.

**Akzeptanzkriterien:**
- [ ] Sessions 1–3: Pause = 5 min (300 Sekunden)
- [ ] Session 4: Pause = 15 min (900 Sekunden)
- [ ] Session 5: Wieder 5 min (Zyklus startet neu)
- [ ] Phasen-Label zeigt „LANGE PAUSE" bei der 15-min-Pause

**Tests:**
- `test_break_duration_normal` → nach Session 1 → 300s
- `test_break_duration_long_after_four` → nach Session 4 → 900s
- `test_break_duration_resets_after_cycle` → nach Session 5 → 300s

**DoD:**
- Logik in `timer.py` erweitert (testbar)
- 3 neue Tests grün (Gesamt: 14)
- UI zeigt „LANGE PAUSE" korrekt
- ruff sauber
- PR gemergt

**VS Code Hinweis:**
- `get_phase_duration()` braucht jetzt einen zweiten Parameter: `sessions_completed`. Die bestehenden Tests aus Issue #5 müssen angepasst werden – das ist normal und kein Fehler!

---

### 📦 Phase F: Dokumentation & Release

#### Issue #12: `docs: README mit Beschreibung, Setup und Screenshot`

**Beschreibung:** README.md ausfüllen nach REPO_README_TEMPLATE: Projektbeschreibung, Installationsanleitung, Beispiel-Ausgabe/Screenshot, „Was ich gelernt habe".

**Akzeptanzkriterien:**
- [ ] Projektbeschreibung erklärt in 2–3 Sätzen was FocusForge tut
- [ ] Installationsanleitung funktioniert (git clone → venv → pip install → python main.py)
- [ ] Mindestens ein Screenshot oder eine Beschreibung der Ausgabe
- [ ] „Was ich gelernt habe"-Abschnitt ist ausgefüllt
- [ ] Badges sichtbar (Python, MIT, Ruff)

**Tests:** Keine (Dokumentation). Aber: Installationsanleitung einmal selbst durchgehen.

**DoD:**
- README vollständig und aktuell
- PR gemergt

**VS Code Hinweis:**
- Markdown-Vorschau: Datei öffnen → `Ctrl+Shift+V` → Live-Vorschau des formatierten Textes

---

#### Issue #13: `docs: CHANGELOG für v0.1.0 erstellen`

**Beschreibung:** CHANGELOG.md nach CHANGELOG_TEMPLATE ausfüllen. Alle Features aus Issues #1–#9 unter v0.1.0 dokumentieren.

**Akzeptanzkriterien:**
- [ ] Keep-a-Changelog-Format eingehalten
- [ ] Alle MVP-Features unter `[0.1.0]` mit Datum eingetragen
- [ ] Vergleichs-Link am Ende korrekt

**Tests:** Keine.

**DoD:**
- CHANGELOG aktuell
- PR gemergt

**VS Code Hinweis:** Keine besonderen Schritte.

---

#### Issue #14: `chore: Release v0.1.0 erstellen`

**Beschreibung:** Git-Tag `v0.1.0` setzen und auf GitHub einen Release veröffentlichen.

**Akzeptanzkriterien:**
- [ ] Tag `v0.1.0` existiert im Repo
- [ ] GitHub Release „v0.1.0 – Pomodoro-Timer Grundgerüst" ist veröffentlicht
- [ ] Release-Beschreibung enthält die CHANGELOG-Einträge

**Tests:** Keine.

**DoD:**
- Tag gepusht
- Release auf GitHub veröffentlicht

**VS Code Hinweis:**
- Tag erstellen: Terminal → `git tag -a v0.1.0 -m "v0.1.0 – Grundgerüst"` → `git push origin v0.1.0`
- Release auf GitHub: Repo → Releases → „Draft a new release" → Tag auswählen

---

#### Issue #15: `docs: CHANGELOG für v0.2.0 und Release`

**Beschreibung:** Should-Features (Issues #10–#11) im CHANGELOG unter v0.2.0 dokumentieren. Release v0.2.0 erstellen.

**Akzeptanzkriterien:**
- [ ] CHANGELOG enthält v0.2.0-Block mit Sound und langer Pause
- [ ] Tag `v0.2.0` existiert
- [ ] GitHub Release veröffentlicht

**Tests:** Keine.

**DoD:**
- CHANGELOG aktuell
- Tag und Release erstellt
- PR gemergt

---

## 10) Testplan

### Unit-Tests (automatisch, pytest)

Getestet wird **ausschließlich `timer.py`** – die reine Logik ohne GUI-Abhängigkeit.

| Funktion | Was wird geprüft? | Anzahl Tests |
|----------|-------------------|:------------:|
| `format_time()` | Sekunden → „MM:SS", Grenzwerte, negative Werte | 5 |
| `get_next_phase()` | Phasenwechsel focus↔break | 2 |
| `get_phase_duration()` | Korrekte Dauer pro Phase + lange Pause | 5 |
| Session-Zähler-Logik | Inkrement nach Fokus, kein Inkrement nach Pause | 2 |

**Minimalziel MVP:** 9 Tests (Issues #4 + #5 + #9)
**Ziel nach v0.2.0:** 14 Tests (+ Issue #11)

### Integration/Smoke-Tests (manuell)

| Was? | Wie prüfen? |
|------|-------------|
| App startet | `python src/focus_forge/main.py` → Fenster geht auf |
| Timer läuft | Start klicken → Countdown zählt runter |
| Phasenwechsel | Timer bis 00:00 laufen lassen (mit kurzer Dauer) → Phase wechselt |
| Reset | Reset in verschiedenen Zuständen klicken |
| Session-Zähler | Fokus-Phase abschließen → Zähler steigt |

### Kommandos

```bash
pytest -v                       # Alle Tests
pytest -v -k "format_time"     # Nur format_time-Tests
pytest -v --tb=short            # Kompakte Fehlerausgabe
ruff check .                    # Linter prüfen
ruff format .                   # Code formatieren
```

---

## 11) Release-Plan

### v0.1.0 – MVP: Pomodoro-Timer Grundgerüst

**Inhalt:** Issues #1–#9 + #12–#14
**Features:** Timer starten/pausieren/resetten, Phasenwechsel, Session-Zähler, Dokumentation.
**Kriterium:** Alle 9 Akzeptanzkriterien aus Abschnitt 4 erfüllt, 9 Tests grün.

### v0.2.0 – Polish: Sound & lange Pause

**Inhalt:** Issues #10–#11 + #15
**Features:** Akustisches Signal, 15-min-Pause nach 4 Sessions.
**Kriterium:** 14 Tests grün, Sound funktioniert, Fehlerfall abgefangen.

### v1.0.0 – Finale Version (optional)

**Kriterien für v1.0.0:**
- Konfigurierbare Zeiten (Fokus/Pause frei wählbar)
- Tages-Statistik mit Persistenz
- Dark/Light Mode
- Keyboard-Shortcuts
- Projekt-Fazit geschrieben

> v1.0.0 ist optional. Wenn du nach v0.2.0 bereit für Projekt 2 (SnakePulse) bist, ist das völlig in Ordnung.

---

## 12) Lernziele (Python-Konzepte konkret)

### Python-Sprache

| Konzept | Wo im Projekt? | Konkretes Beispiel |
|---------|----------------|--------------------|
| **Variablen & Datentypen** | Timer-State | `time_remaining: int = 1500`, `is_running: bool = False` |
| **f-Strings** | Zeitformatierung | `f"{minutes:02d}:{seconds:02d}"` |
| **Ganzzahl-Division & Modulo** | Sekunden → Minuten | `minutes = seconds // 60`, `secs = seconds % 60` |
| **if/elif/else** | Phasenwechsel, Validierung | `if phase == "focus": return "break"` |
| **Funktionen (def)** | Gesamte Logik | `def format_time(seconds: int) -> str:` |
| **Parameter & Rückgabewerte** | Alle Logik-Funktionen | Eingabe → Verarbeitung → Return |
| **Module / import** | Trennung Logik↔UI | `from focus_forge.timer import format_time` |
| **async/await (Einstieg)** | Timer-Loop in Flet | `async def tick(): await asyncio.sleep(1)` |

### Engineering & Tooling

| Konzept | Wo im Projekt? |
|---------|---------------|
| Erstes GitHub-Repo anlegen | Issue #1 |
| Erster Branch + erster PR | Issue #2 |
| Erste pytest-Tests schreiben | Issue #4 |
| ruff als Linter nutzen | Jedes Issue |
| Logik sauber vom GUI trennen | `timer.py` vs. `main.py` |
| PR-Checkliste durchgehen | Jeder PR |
| Git Tag + GitHub Release | Issue #14 |
| Debugger mit Breakpoints nutzen | Issue #5 (Logik inspizieren) |

---

## 13) Stretch Goals

1. **Keyboard-Shortcuts:** Leertaste = Start/Pause, R = Reset
2. **Fenstertitel-Timer:** Titel zeigt verbleibende Zeit (z.B. „FocusForge – 12:45")
3. **Tages-Statistik:** Sessions und Fokus-Minuten pro Tag anzeigen
4. **Konfigurierbare Zeiten:** Slider oder Dropdown für Fokus-/Pausen-Dauer
5. **Export:** Tages-Daten als CSV oder JSON speichern
6. **Mini-Modus:** Kompaktes Overlay-Fenster das immer im Vordergrund bleibt

---

## 14) Risiken & typische Anfängerfehler

| # | Risiko | Was passiert? | Gegenmaßnahme |
|---|--------|--------------|---------------|
| 1 | **Timer-Drift** | `time.sleep(1)` ist nicht exakt – nach 25 min kann der Timer Sekunden abweichen | Echte Zeitvergleiche (`time.time()`-Differenz) statt Sleep-Counter verwenden, oder Flets eingebauten async-Timer nutzen |
| 2 | **GUI friert ein** | Timer läuft im Haupt-Thread → Fenster reagiert nicht mehr | `async`/`await` mit Flets `page.run_task()` nutzen, **niemals** `time.sleep()` im Haupt-Thread |
| 3 | **Alles in einer Datei** | Gesamte Logik + UI in `main.py` → nichts ist testbar | Von Anfang an `timer.py` als separates Modul. Issue #4 erzwingt das |
| 4 | **Zu großes MVP** | Sound, Statistik, Config gleichzeitig anfangen → nichts wird fertig | Strikt Issues #1–#9 zuerst. Should-Features erst in v0.2.0 |
| 5 | **venv vergessen** | Pakete global installieren statt in der virtuellen Umgebung | Immer `(.venv)` am Terminal-Prompt prüfen vor `pip install` |
| 6 | **Kein Commit nach Feature** | Stundenlang coden ohne zu committen → Fortschritt geht verloren | Faustregel: Ein Issue = ein Branch = ein PR. Nach jedem grünen Test: committen |
| 7 | **Tests auslassen** | „Funktioniert ja, brauche keine Tests" → Fehler schleichen sich ein | Issue #4 macht Tests zum Pflicht-Issue bevor GUI-Features kommen |
| 8 | **State-Chaos** | Phasen-Label sagt „PAUSE" aber Timer zeigt Fokus-Dauer → UI und Daten sind unsynchron | Alle State-Änderungen über eine zentrale Update-Funktion, die IMMER alle UI-Elemente aktualisiert |
| 9 | **Fehlende Validierung** | Negative Sekunden, unbekannte Phase → kryptischer Crash | `format_time` fängt negative Werte ab (Issue #4), `get_next_phase` hat nur 2 gültige Inputs |

---

## 15) CI-Hinweis

**Lokal testen immer. GitHub Actions (CI) können wir sofort aktivieren oder später – je nach Lernstand.**

Die CI-Datei `ci.yml.disabled` liegt von Anfang an im Repo als Referenz. CI wird aktiviert, sobald Philipp pytest und ruff lokal sicher beherrscht und erklären kann, was CI tut.

---

## Save-Liste

Lege folgende Datei an:

```
/projects/P01_FocusForge/BLUEPRINT.md
```
