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

    # TODO: UI-Elemente hinzufügen (Issue #3)
    page.add(
        ft.Text("FocusForge 🔨", size=32, weight=ft.FontWeight.BOLD)
    )


if __name__ == "__main__":
    ft.app(target=main)
