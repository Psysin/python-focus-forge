"""Main entry point for FocusForge application.

This module contains the Flet UI code.
"""

import asyncio

import flet as ft

from focus_forge.timer import format_time


def main(page: ft.Page):
    """Main function to build the Flet app."""
    page.title = "FocusForge"
    page.window.width = 400
    page.window.height = 450
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # State Variabklen (Zustand)
    time_remaining = 1500  # Startwert 25 Minuten in Sekunden
    is_running = False  # Timer läuft noch nicht

    # Funktion für den Timer
    async def timer_loop():
        nonlocal time_remaining, is_running
        while is_running and time_remaining > 0:
            await asyncio.sleep(1)
            time_remaining -= 1
            countdown.value = format_time(time_remaining)
            countdown.update()

    # Funktion für Toggle
    # Einfache Funktion, das Atribut e in Klammern Bedeutet Event z.B. der Klick
    def toggle_timer(e):
        # nonlocal bedeutet, das eine Variable außerhalb der Funktion genutzt wird
        nonlocal is_running
        # Umschalten True/False
        is_running = not is_running
        if is_running:
            # Button Text ändern
            btn_start.text = "⏸ Pause"
            # Async Timer-Loop Starten
            page.run_task(timer_loop)
        else:
            btn_start.text = "▶ Start"
            # Änderung auf Bildschirm anzeigen
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
    btn_start_label = ft.Text("▶ Start")
    btn_start = ft.ElevatedButton(
        content=btn_start_label, on_click=toggle_timer
    )  # On_Click sagt tut hier etwas bei einen Click, starte die Funktion toggle_timer
    btn_reset = ft.ElevatedButton("↺ Reset")

    # Fügt ein weiteres Anzeige-Element mit Counter hinzu
    session_label = ft.Text("Sessions heute: 0", size=14)

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
    ft.app(target=main)
