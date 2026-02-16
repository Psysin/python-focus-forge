# Contributing to FocusForge

Danke für dein Interesse an FocusForge! Dieses Projekt ist Teil meiner Python Learning Journey.

## 🔧 Entwicklungsumgebung einrichten

1. Fork das Repository
2. Clone deinen Fork:
   ```bash
   git clone https://github.com/DEIN-USERNAME/python-focus-forge.git
   cd python-focus-forge
   ```

3. Virtuelle Umgebung erstellen:
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1  # Windows
   # oder: source .venv/bin/activate  # Linux/Mac
   ```

4. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

## 🌿 Branching-Strategie

- `main` - Produktionsreifer Code
- `feat/beschreibung` - Neue Features
- `fix/beschreibung` - Bugfixes
- `docs/beschreibung` - Dokumentation

## ✅ Before Submitting a PR

1. **Tests ausführen:**
   ```bash
   pytest -v
   ```

2. **Code-Qualität prüfen:**
   ```bash
   ruff check .
   ruff format .
   ```

3. **Commit-Messages:** Verwende das Format:
   - `feat: Beschreibung` - Neue Features
   - `fix: Beschreibung` - Bugfixes
   - `docs: Beschreibung` - Dokumentation
   - `test: Beschreibung` - Tests
   - `chore: Beschreibung` - Wartung

## 📋 Pull Request Prozess

1. Erstelle einen Branch für deine Änderung
2. Implementiere deine Changes
3. Stelle sicher, dass alle Tests grün sind
4. Erstelle einen Pull Request mit klarer Beschreibung

## 🧪 Tests schreiben

Tests gehören in den `tests/` Ordner. Jeder Test sollte:
- Mit `test_` beginnen
- Eine klare Beschreibung haben
- Nur eine Sache testen (Single Responsibility)

Beispiel:
```python
def test_format_time_full_minutes():
    """Test: 1500 Sekunden = 25:00"""
    assert format_time(1500) == "25:00"
```

## 💡 Tipps

- Halte PRs klein und fokussiert
- Schreibe selbsterklärenden Code
- Kommentiere nur, was nicht offensichtlich ist
- Folge dem bestehenden Code-Stil

## ❓ Fragen?

Öffne ein Issue auf GitHub!
