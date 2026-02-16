# 🔨 FocusForge

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Ein Pomodoro-Timer mit Flet-GUI – starte 25-Minuten-Fokus-Sessions, mach 5 Minuten Pause, und behalte den Überblick über deine Produktivität.

## 🎯 Features

- ⏱️ 25-Minuten Fokus-Phasen
- ☕ 5-Minuten Pausen
- 🔄 Automatischer Phasenwechsel
- 📊 Session-Zähler
- 🎨 Übersichtliche GUI mit Flet

## 🚀 Installation

```bash
# Repository klonen
git clone https://github.com/DEIN-USERNAME/python-focus-forge.git
cd python-focus-forge

# Virtuelle Umgebung erstellen
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
# oder: source .venv/bin/activate  # Linux/Mac

# Abhängigkeiten installieren
pip install -r requirements.txt

# App starten
python src/focus_forge/main.py
```

## 📖 Verwendung

1. Klicke auf "▶ Start", um eine Fokus-Session zu beginnen
2. Der Timer zählt 25 Minuten herunter
3. Nach Ablauf wechselt die App automatisch in die Pause (5 Minuten)
4. Der Session-Zähler zeigt deine abgeschlossenen Fokus-Runden

## 🧪 Tests ausführen

```bash
pytest -v
```

## 🔧 Code-Qualität prüfen

```bash
ruff check .
ruff format .
```

## 📝 Was ich gelernt habe

_Dieser Abschnitt wird nach Projektabschluss ausgefüllt._

## 📄 Lizenz

MIT License - siehe [LICENSE](LICENSE) für Details.

## 🙏 Danksagung

Projekt 01 der Python Learning Journey.
