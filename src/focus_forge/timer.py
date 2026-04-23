"""Timer logic module.

This module contains pure functions for timer calculations.
No GUI dependencies - fully testable.
"""

# Konstanten
FOCUS_DURATION_SEC = 1500  # 1500 25 MinutenS
BREAK_DURATION_SEC = 300  # 300 5 Minuten
LONG_BREAK_DURATION_SEC = 90  # 900 15 Minuten
SESSIONS_BEFORE_LONG_BREAK = 4


# Wir übergeben der Funktion Sekunden in Int und erhalten den Output in STR
def format_time(seconds: int) -> str:
    """Convert seconds to MM:SS format.

    Args:
        seconds: Number of seconds to format

    Returns:
        String in MM:SS format

    Examples:
        >>> format_time(1500)
        '25:00'
        >>> format_time(90)
        '01:30'
    """
    # Implementierung (Issue #4)
    if seconds < 0:
        return "00:00"
    minutes = seconds // 60
    secs = seconds % 60
    # Bei return lässt man die Klammern weg für gewöhnlich
    return f"{minutes:02}:{secs:02}"


def get_next_phase(current_phase: str) -> str:
    """Get the next phase after the current one.

    Args:
        current_phase: Either "focus" or "break"

    Returns:
        The next phase ("focus" or "break")

    Examples:
        >>> get_next_phase("focus")
        'break'
        >>> get_next_phase("break")
        'focus'
    """
    # TODO: Implementierung (Issue #5)
    if current_phase == "focus":
        return "break"
    elif current_phase == "break":
        return "focus"
    else:
        raise ValueError(f"Unbekannte Phase: {current_phase}!")


def get_phase_duration(phase: str) -> int:
    """Get the duration in seconds for a given phase.

    Args:
        phase: Either "focus" or "break"

    Returns:
        Duration in seconds

    Examples:
        >>> get_phase_duration("focus")
        1500
        >>> get_phase_duration("break")
        300
    """
    # TODO: Implementierung (Issue #5)
    if phase == "focus":
        return FOCUS_DURATION_SEC
    elif phase == "break":
        return BREAK_DURATION_SEC
    else:
        raise ValueError(f"Unbekannte Phase: {phase}")


# Funktion zum prüfen welche Pause aktiv ist, lang oder kurz
def get_break_duration(session_count: int) -> int:
    # Wir schauen ob die vierte pause erreicht wurde, wenn ja dann lange Pause
    if session_count % 4 == 0 and session_count != 0:
        return LONG_BREAK_DURATION_SEC
    else:
        return BREAK_DURATION_SEC
