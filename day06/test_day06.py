import day06

def test_get_data():
    assert day06.get_data("Distance:  9  40  200") == [9, 40,200]

def test_distance_no_hold():
    assert day06.travel_distance(7,0) == 0

def test_distance_hold_forever():
    assert day06.travel_distance(7,7) == 0

def test_distance_hold_for_time():
    assert day06.travel_distance(7,4) == 12

def test_winning_options():
    assert day06.winning_options(7,9,"A") == 4