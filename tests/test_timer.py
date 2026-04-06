"""Tests for timer.py logic."""

import pytest
from focus_forge.timer import format_time, get_next_phase, get_phase_duration


# TODO: Issue #4 - Tests für format_time()
def test_format_time_full_minutes():
#     """Test: 1500 Sekunden = 25:00"""
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
# def test_next_phase_focus_to_break():
#     """Test: Nach Focus kommt Break"""
#     assert get_next_phase("focus") == "break"


# TODO: Issue #5 - Tests für get_phase_duration()
# def test_duration_focus():
#     """Test: Focus-Phase dauert 1500 Sekunden"""
#     assert get_phase_duration("focus") == 1500
