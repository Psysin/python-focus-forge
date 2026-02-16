# ðŸ™ GITHUB PLAYBOOK

> Alles rund um GitHub: Repos organisieren, Issues verwalten, PRs richtig machen,
> Releases verÃ¶ffentlichen und CI verstehen.

---

## 1. Repo-Struktur & Organisation

### 1.1 Dein GitHub-Profil

Dein GitHub-Profil ist dein Entwickler-Portfolio. Jedes Lernprojekt wird ein eigenes
Repository. Ãœber die Zeit entsteht so eine sichtbare Dokumentation deiner Lernreise.

### 1.2 Repo-Naming

Folge den Konventionen aus ROADMAP_MASTER.md:

```
python-focus-forge       â† Software (Flet GUI)
python-snake-pulse       â† Spiel (Pygame)
python-pocket-tasks      â† Software (Flet GUI)
python-flappy-bounce     â† Spiel (Pygame)
```

### 1.3 Repo-Settings (bei jedem neuen Repo)

Beim Erstellen auf GitHub:

- **Visibility:** Public (deine Lernreise darf sichtbar sein â€“ das zeigt Engagement!)
- **Initialize with:** README âœ…, .gitignore (Python) âœ…, License (MIT) âœ…
- **Default branch:** `main`

Nach dem Erstellen unter â€žSettings â†’ General":

- **Features:** Issues âœ… aktiviert
- **Pull Requests:** â€žAllow squash merging" âœ… (fÃ¼r saubere History)
- **Automatically delete head branches:** âœ… (Feature-Branches nach Merge aufrÃ¤umen)

---

## 2. Projektmanagement mit Issues

### 2.1 Was ist ein Issue?

Ein Issue ist eine Aufgabe, ein Bug, ein Feature-Wunsch oder eine Frage.
FÃ¼r uns ist ein Issue = eine klar definierte Arbeitseinheit.

**Goldene Regel:** Bevor du Code schreibst, gibt es ein Issue dafÃ¼r.

### 2.2 Labels

Labels kategorisieren deine Issues. Erstelle diese Labels in jedem neuen Repo:

| Label | Farbe (Hex) | Bedeutung |
|-------|-------------|-----------|
| `feature` | `#0E8A16` (grÃ¼n) | Neues Feature oder FunktionalitÃ¤t |
| `bug` | `#D73A4A` (rot) | Etwas funktioniert nicht richtig |
| `docs` | `#0075CA` (blau) | Nur Dokumentation betroffen |
| `refactor` | `#E4E669` (gelb) | Code umstrukturieren, keine neue Funktion |
| `test` | `#BFD4F2` (hellblau) | Tests hinzufÃ¼gen oder verbessern |
| `learning` | `#F9D0C4` (rosa) | Lernnotiz: Etwas Neues verstanden |
| `good first issue` | `#7057FF` (lila) | Einstiegspunkt (fÃ¼r dich selbst als Erinnerung) |
| `blocked` | `#B60205` (dunkelrot) | Kann gerade nicht bearbeitet werden |
| `priority: high` | `#FF6600` (orange) | Wichtig, bald erledigen |
| `priority: low` | `#CCCCCC` (grau) | Kann warten |

**Labels auf GitHub erstellen:**
Repo â†’ Issues â†’ Labels â†’ â€žNew label"

### 2.3 Milestones

Ein Milestone gruppiert zusammengehÃ¶rige Issues zu einem Ziel.

**FÃ¼r Lernprojekte sinnvoll:**

```
Milestone: v0.1.0 â€“ GrundgerÃ¼st
  â”œâ”€â”€ Issue #1: Projektstruktur anlegen
  â”œâ”€â”€ Issue #2: Grundfunktion implementieren
  â””â”€â”€ Issue #3: Erste Tests schreiben

Milestone: v1.0.0 â€“ Feature-komplett
  â”œâ”€â”€ Issue #4: Feature X hinzufÃ¼gen
  â”œâ”€â”€ Issue #5: Feature Y hinzufÃ¼gen
  â””â”€â”€ Issue #6: README finalisieren
```

**Milestone erstellen:**
Repo â†’ Issues â†’ Milestones â†’ â€žNew milestone"
- Titel: z.B. `v0.1.0 â€“ GrundgerÃ¼st`
- Beschreibung: Was soll am Ende funktionieren?
- Deadline: Optional (bei Lernprojekten eher weglassen)

### 2.4 Issue schreiben (Best Practices)

Ein gutes Issue enthÃ¤lt:

1. **Klaren Titel:** Was soll passieren? (z.B. â€žTimer starten und stoppen kÃ¶nnen")
2. **Beschreibung:** Kontext und Details
3. **Akzeptanzkriterien:** Wann ist das Issue fertig? (Checkliste)
4. **Labels:** Mindestens ein Typ-Label
5. **Milestone:** Zugeordnet wenn passend

> **Nutze die Issue-Templates!** Sie geben dir eine Struktur vor.
> Siehe `/templates/ISSUE_TEMPLATES.md` fÃ¼r die Vorlagen.

---

## 3. Pull Request Workflow

### 3.1 Warum PRs bei Solo-Arbeit?

Ein PR ist dein persÃ¶nlicher Code-Review-Moment. Bevor Code in `main` landet,
schaust du nochmal drÃ¼ber und prÃ¼fst systematisch, ob alles stimmt.

### 3.2 PR erstellen

1. Arbeite in deinem Feature-Branch
2. Pushe den Branch auf GitHub
3. GitHub zeigt â€žCompare & pull request" â†’ klicken
4. **Titel:** `feat: Add timer start/stop (#3)` (Issue-Nummer verlinken!)
5. **Beschreibung:** Nutze das PR-Template (wird automatisch geladen)
6. **Rechte Seite:** Labels, Milestone, ggf. Issue verlinken

### 3.3 PR-Template Logik

Das PR-Template (siehe `/templates/PR_TEMPLATE.md`) enthÃ¤lt eine Checkliste.
Bei Solo-Arbeit bist du selbst der Reviewer, darum ist die Checkliste dein Sicherheitsnetz.

**Die Checkliste prÃ¼ft:**
- Ist der Code getestet?
- LÃ¤uft der Linter sauber?
- Sind keine Secrets im Code?
- Ist die Beschreibung verstÃ¤ndlich?
- Passt der Code zur Issue-Anforderung?

### 3.4 Self-Review Workflow

Bevor du â€žMerge" klickst:

1. **Files Changed Tab** Ã¶ffnen â†’ Lies deinen eigenen Code als wÃ¤re er von jemand anderem
2. Stell dir vor, du siehst den Code zum ersten Mal: Verstehst du ihn?
3. Gibt es auskommentierte Zeilen? â†’ LÃ¶schen
4. Gibt es `print()`-Statements, die nur zum Debuggen da waren? â†’ LÃ¶schen
5. Laufen alle Tests? â†’ Terminal: `pytest -v`
6. Linter sauber? â†’ Terminal: `ruff check .`
7. Alles grÃ¼n? â†’ Merge!

### 3.5 Merge-Strategie

Wir nutzen **Squash and Merge:**
- Alle Commits des Branches werden zu einem einzigen Commit zusammengefasst
- Die `main`-History bleibt sauber und Ã¼bersichtlich
- Jeder Eintrag auf `main` = ein Feature / Bugfix / etc.

---

## 4. Releases, Tags & Changelog

### 4.1 Was ist ein Release?

Ein Release ist ein Snapshot deines Projekts zu einem bestimmten Zeitpunkt.
Es sagt: â€žHier ist Version X, und das kann sie."

### 4.2 Wann ein Release erstellen?

- Nach Abschluss eines Milestones
- Wenn eine sinnvolle Menge an Features fertig ist
- Beim Abschluss des Projekts

### 4.3 Release erstellen

**Schritt 1: Tag erstellen**
```bash
git tag -a v0.1.0 -m "v0.1.0 â€“ GrundgerÃ¼st"
git push origin v0.1.0
```

**Was ist ein Tag?** Ein benannter Marker an einem bestimmten Commit.
Wie ein Lesezeichen in der Git-Geschichte.

**Schritt 2: Release auf GitHub**
1. Repo â†’ Releases â†’ â€žDraft a new release"
2. Tag auswÃ¤hlen: `v0.1.0`
3. Titel: `v0.1.0 â€“ GrundgerÃ¼st`
4. Beschreibung: Aus dem CHANGELOG.md kopieren
5. â€žPublish release"

### 4.4 Changelog pflegen

Der CHANGELOG.md wird bei jedem Merge auf `main` aktualisiert.
Siehe `/templates/CHANGELOG_TEMPLATE.md` fÃ¼r das Format.

**Wann aktualisieren?**
- Idealerweise: Als Teil des PR (letzte Ã„nderung vor dem Merge)
- Mindestens: Vor einem Release

---

## 5. CI (Continuous Integration) â€“ Ãœberblick

### 5.1 Was ist CI?

CI = **Continuous Integration** = Kontinuierliche Integration.

Jedes Mal, wenn du Code auf GitHub pushst, startet automatisch ein Prozess, der:
1. Deinen Code auscheckt
2. Python und deine Pakete installiert
3. Den Linter ausfÃ¼hrt (`ruff check .`)
4. Deine Tests ausfÃ¼hrt (`pytest`)
5. Dir das Ergebnis als grÃ¼nes âœ… oder rotes âŒ zeigt

### 5.2 Warum ist das nÃ¼tzlich?

| Vorteil | ErklÃ¤rung |
|---------|-----------|
| **Sicherheitsnetz** | Selbst wenn du lokal vergisst Tests zu starten â€“ CI vergisst nie |
| **Reproduzierbarkeit** | CI testet in einer frischen Umgebung (nicht dein lokaler PC) |
| **Vertrauen** | GrÃ¼nes âœ… am PR heiÃŸt: Tests und Linter sind OK |
| **Professionell** | So arbeiten echte Teams â€“ du lernst es von Anfang an |

### 5.3 Wie sieht das aus?

```
Du pushst Code â†’ GitHub Actions startet â†’ Pipeline lÃ¤uft â†’ âœ… oder âŒ

Im PR siehst du dann:
  âœ… CI / test (3.12) â€“ All checks have passed
  oder
  âŒ CI / test (3.12) â€“ 2 tests failed
```

### 5.4 Unsere CI-Timing-Regel

> **CI ist Standard, aber die Aktivierung folgt deinem Lernstand.**

Am Anfang testest du **lokal** mit `pytest` und `ruff`. Die CI-Konfigurationsdatei
liegt schon im Repo (als Referenz), wird aber erst aktiviert, wenn du die Tools
lokal sicher beherrschst.

**Siehe ROADMAP_MASTER.md â†’ Abschnitt 7** fÃ¼r die vollstÃ¤ndige CI-Timing-Regel.

### 5.5 Was du schon wissen solltest

Die CI-Konfiguration ist eine YAML-Datei unter `.github/workflows/ci.yml`.
Du musst sie nicht auswendig kennen â€“ Claude Code erstellt sie beim Projekt-Setup.
Aber es ist gut zu wissen, dass sie existiert und was sie tut.

**Siehe `/templates/CI_WORKFLOW_TEMPLATE.yml`** fÃ¼r ein kommentiertes Beispiel.

---

## 6. GitHub-Etikette (auch als Solo-Entwickler)

### Gute Gewohnheiten, die sich auszahlen:

1. **Jedes Issue vor dem Coden erstellen** â€“ SchÃ¤rft dein Denken
2. **AussagekrÃ¤ftige Commit-Messages** â€“ Dein zukÃ¼nftiges Ich wird dankbar sein
3. **PRs mit Beschreibung** â€“ Auch wenn du der Einzige bist, der sie liest
4. **CHANGELOG pflegen** â€“ Zeigt professionelle Arbeitsweise
5. **README aktuell halten** â€“ Ist die Visitenkarte deines Projekts
6. **Keine Secrets committen** â€“ Auch nicht â€žnur kurz zum Testen"

---

*Letzte Aktualisierung: 2026-02-13*
