"""Timer logic module.

This module contains pure functions for timer calculations.
No GUI dependencies - fully testable.
"""

# Konstanten
FOCUS_DURATION_SEC = 1500  # 25 Minuten
BREAK_DURATION_SEC = 300   # 5 Minuten
LONG_BREAK_DURATION_SEC = 900  # 15 Minuten
SESSIONS_BEFORE_LONG_BREAK = 4


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
    # TODO: Implementierung (Issue #4)
    pass


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
    pass


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
    pass
