"""Main entry point for FocusForge application.

This module contains the Flet UI code.
"""

import flet as ft


def main(page: ft.Page):
    """Main function to build the Flet app."""
    page.title = "FocusForge"
    page.window.width = 400
    page.window.height = 450
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

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
    btn_start = ft.ElevatedButton("▶ Start")
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
