import day11

def test_insert_rows():
    data = ["#.........","..........","......#..."]
    assert day11.insert_rows(data) == [1]

def test_insert_columns():
    data = ["#...","....","..#."]
    assert day11.insert_columns(data) == [1,3]

def test_get_galaxies():
    data = ["#...","....","..#."]
    assert day11.get_galaxies(data,[1],[1,3],"A") == [(0,0),(3,3)]

def test_calc_distance():
    assert day11.calc_distance((0,2),(2,0)) == 4

def test_sum_shortest_paths():
    assert day11.sum_shortest_paths([(0,2),(2,0),(3,3)]) == 12