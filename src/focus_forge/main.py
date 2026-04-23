"""Main entry point for FocusForge application.

This module contains the Flet UI code.
"""

import asyncio
from pathlib import Path

import flet as ft
import pygame

from focus_forge.timer import (
    FOCUS_DURATION_SEC,
    format_time,
    get_break_duration,
    get_next_phase,
    get_phase_duration,
)


def main(page: ft.Page):
    """Main function to build the Flet app."""
    page.title = "FocusForge"
    page.window.width = 400
    page.window.height = 450
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Pfad zur Sounddatei
    sound_path = Path(__file__).parent.parent.parent / "assets" / "sounds" / "whoosh.mp3"

    # Pygame Initialisieren
    # Mit Try/except sicherstellen das bei fehlendem Sound kmein Fehler kommt
    try:
        pygame.mixer.init()
        sound = pygame.mixer.Sound(sound_path)
    except Exception:
        sound = None

    # State Variabklen (Zustand)
    time_remaining = FOCUS_DURATION_SEC  # Startwert 25 Minuten in Sekunden
    is_running = False  # Timer läuft noch nicht
    current_phase = "focus"
    session_count = 0  # Aktuelle Phase

    # Funktion für den Timer
    async def timer_loop():
        nonlocal time_remaining, is_running, current_phase, session_count  # ← bleibt!
        while is_running and time_remaining > 0:
            time_remaining -= 1
            countdown.value = format_time(time_remaining)
            countdown.update()
            await asyncio.sleep(1)
        # Abfrage die Prüft, ob der Timer auf 0 gelaufen ist um dann den Phasencounter
        # zu erhöhen
        if time_remaining == 0:
            if current_phase == "focus":
                session_count += 1
                # Bei Zuweisung brauchen wir keine Klammern im f-String
                session_label.value = f"Sessions heute {session_count}"
                page.update()
            current_phase = get_next_phase(current_phase)
            if current_phase == "break":
                time_remaining = get_break_duration(session_count)
            else:
                time_remaining = get_phase_duration(current_phase)
            if current_phase == "focus":
                phase_label.value = "FOKUS"
                phase_label.color = "blue"
            else:
                phase_label.value = "PAUSE"
                phase_label.color = "red"
            # Da das page.update jeden Phasenwechsel auslößt, sollte hier auch der Sound liegen
            if sound is not None:
                sound.play()
            page.update()
            is_running = True
            page.run_task(timer_loop)

    # Funktion für Toggle
    # Einfache Funktion, das Atribut e in Klammern Bedeutet Event z.B. der Klick
    def toggle_timer(e):
        # nonlocal bedeutet, das eine Variable außerhalb der Funktion genutzt wird
        nonlocal is_running
        # Umschalten True/False
        is_running = not is_running
        if is_running:
            # Button Text ändern
            btn_start_text.value = "⏸ Pause"
            # Async Timer-Loop Starten
            page.run_task(timer_loop)
        else:
            btn_start_text.value = "▶ Start"
            # Änderung auf Bildschirm anzeigen
        page.update()

    # Funktion für Reset
    def reset_timer(e):
        nonlocal is_running, time_remaining
        is_running = False
        btn_start_text.value = "▶ Start"
        countdown.value = format_time(FOCUS_DURATION_SEC)
        time_remaining = FOCUS_DURATION_SEC
        page.update()

    # Fügt ein Label ein mit Text und gibt Größe und Farbe an.
    # Wir greifen hier auf Objekte von ft (flet) zu per .
    phase_label = ft.Text(
        "FOKUS",
        size=24,
        color="Blue",
        weight=ft.FontWeight.BOLD,
    )
    # Fügt ein Anzeige-Element mit Startwert für Contdown ein und setzt Font Styles
    countdown = ft.Text(
        "25:00",
        size=72,
        weight=ft.FontWeight.BOLD,
    )
    # Fügt die Buttons hinzu mit Beschriftung
    btn_start_text = ft.Text("▶ Start")
    btn_start = ft.Button(content=btn_start_text, on_click=toggle_timer)
    btn_reset_text = ft.Text("↺ Reset")
    btn_reset = ft.Button(content=btn_reset_text, on_click=reset_timer)

    # Fügt ein weiteres Anzeige-Element mit Counter hinzu
    session_label = ft.Text(f"Sessions heute: {session_count}", size=14)

    # Wir gruppieren alle Elemente in einer column und fügen sie der Seite hinzu
    page.add(
        ft.Column(
            [
                phase_label,
                countdown,
                ft.Row(
                    [btn_start, btn_reset],
                    alignment=ft.MainAxisAlignment.CENTER,  # Vertikale Zentrierung
                ),
                session_label,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Horizontale Zentrierung
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    ft.run(main)
