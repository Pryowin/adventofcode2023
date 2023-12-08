import day08

def test_get_location():
    assert day08.get_location("AAA = (BBB, BBB)") == "AAA"

def test_get_left_right():
    assert day08.get_left_right("AAA = (BBB, CCC)") == ["BBB", "CCC"]

def test_get_location_dict():
    assert day08.get_location_dict(["AAA = (BBB, BBB)", "BBB = (AAA, CCC)"]) == {'AAA': ['BBB','BBB'], 'BBB': ['AAA', 'CCC'] }

def test_get_start_locations():
    assert day08.get_start_locations({'AAA': ['BBB','BBB'], 'BBB': ['AAA', 'CCC'], 'ZYA': ['AAA', 'CCC']} ) == ['AAA', "ZYA"]

def test_count_destinations():
    assert day08.count_destinations({'AAA': ['BBB','BBB'], 'BBZ': ['AAA', 'CCC'], 'ZYA': ['AAA', 'CCC']}) == 1