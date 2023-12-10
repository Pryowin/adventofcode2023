import day10
import pytest
import sys

sys.path.append( '../python_modules' )
import advent

def test_get_pipe_ends_vertical():
    assert day10.get_pipe_ends((3,3),"|") == ((3,4),(3,2))

def test_get_pipe_ends_horizontal():
    assert day10.get_pipe_ends((3,3),"-") == ((4,3),(2,3))

def test_get_pipe_ends_90NE():
    assert day10.get_pipe_ends((3,3),"L") == ((4,3),(3,2))

def test_get_pipe_ends_90NW():
    assert day10.get_pipe_ends((3,3),"J") == ((2,3),(3,2))
                                              
def test_get_pipe_ends_90SW():
    assert day10.get_pipe_ends((3,3),"7") == ((2,3),(3,4))

def test_get_pipe_ends_90SE():
    assert day10.get_pipe_ends((3,3),"F") == ((4,3),(3,4))

def test_find_start():
    map = [['.','.','.'],['.','.','S']]
    day10.set_max_dimensions(map)
    assert day10.find_start() == (2,1)

def test_find_start_missing():
    with pytest.raises(Exception):
        day10.find_start([['.','.','.'],['.','.','.']])

def test_find_connected_pipes():
    data = advent.read_input("test.txt")
    field = day10.create_field(data)
    day10.set_max_dimensions(field)
    start = day10.find_start()

    assert day10.find_connected_pipes(start) == ((1,2),(0,3))

