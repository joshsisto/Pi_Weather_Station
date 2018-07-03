import pytest

from code.weather import set_screen_color

def test_set_screen_color():
    assert set_screen_color(25) == [0, 0, 155]
