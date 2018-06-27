import pytest

from weather import *

def test_set_screen_color():
    assert set_screen_color(25) == [0, 0, 155]
    
    
