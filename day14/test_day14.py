import day14
import sys

sys.path.append( '../python_modules' )
import advent

def test_build_platform():
    data = advent.read_input("test.txt")
    grid = day14.build_platform(data)

    assert len(grid) == 10
    assert len(grid[0]) == 10

    assert day14.get_contents(grid, 1, 3) == 1

def test_score_grid():
    data = [[1,-1,0],[1,1,-1]]
    assert day14.score_grid(data) == 4

def test_slide_rocks():
    grid = [[0,1,-1],[0,0,1],[1,0,0]]
    expected = [[0,1, 1],[0,0,-1],[1,0,0]]

    assert day14.slide_rocks(grid) == expected