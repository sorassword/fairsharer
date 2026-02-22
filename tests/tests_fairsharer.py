import pytest
from fairsharer.fair_sharer import fair_sharer

def test_fair_sharer_one_iteration():
    """Testet den Algorithmus mit einer Iteration."""
    initial = [0, 1000, 800, 0]
    expected = [100, 800, 900, 0]
    assert fair_sharer(initial, 1) == expected

def test_fair_sharer_two_iterations():
    """Testet den Algorithmus mit zwei Iterationen."""
    initial = [0, 1000, 800, 0]
    expected = [100, 890, 720, 90]
    assert fair_sharer(initial, 2) == expected

def test_fair_sharer_no_iterations():
    """Testet, ob bei 0 Iterationen die Liste unverändert bleibt."""
    initial = [0, 1000, 800, 0]
    expected = [0, 1000, 800, 0]
    assert fair_sharer(initial, 0) == expected