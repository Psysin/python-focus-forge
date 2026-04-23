"""Tests for timer.py logic."""

from focus_forge.timer import (
    BREAK_DURATION_SEC,
    LONG_BREAK_DURATION_SEC,
    format_time,
    get_break_duration,
    get_next_phase,
    get_phase_duration,
)


# TODO: Issue #4 - Tests für format_time()
def test_format_time_full_minutes():
    assert format_time(1500) == "25:00"


def test_format_time_mixed():
    assert format_time(90) == "01:30"


def test_format_time_zero():
    assert format_time(0) == "00:00"


def test_format_time_large():
    assert format_time(3599) == "59:59"


def test_format_time_negative():
    assert format_time(-5) == "00:00"


# TODO: Issue #5 - Tests für get_next_phase()
def test_next_phase_focus_to_break():

    assert get_next_phase("focus") == "break"


# Test nach break kommt focus
def test_next_phase_break_to_focus():
    assert get_next_phase("break") == "focus"


# Test Duration muss 1500 sein
def test_duration_focus():
    assert get_phase_duration("focus") == 1500


# Test Duration muss 300 sein
def test_duration_break():
    assert get_phase_duration("break") == 300


def test_get_break_duration_normal():
    assert get_break_duration(session_count=2) == BREAK_DURATION_SEC


def test_get_break_duration_normal_0():
    assert get_break_duration(session_count=0) == BREAK_DURATION_SEC


def test_get_break_duration_long():
    assert get_break_duration(session_count=4) == LONG_BREAK_DURATION_SEC
