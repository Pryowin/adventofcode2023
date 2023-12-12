import day12

def test_get_conditions():
    assert day12.get_conditions("???.###  1,1,3") == "???WBBB"

def test_get_size_of_groups():
    assert day12.get_size_of_groups("???.###  1,1,3") == [1,1,3]

def test_build_match_pattern():
    assert day12.build_match_pattern([1,1,3]) == "BW+BW+BBB" 

def test_is_possible_match_true():
    assert day12.is_possible_match("BWBWBBB", "BW+BW+BBB") == True

def test_is_possible_match_not_at_start():
    assert day12.is_possible_match("WWWBWBBBBBWWBBBBW", "BW+BBBBBW+BBBB") == True

def test_is_possible_match_false():
    assert day12.is_possible_match("WWWBBWWWWBBB.", "BW+BW+BBB") == False

def test_convert_condition_to_int():
    assert day12.convert_condition_to_int("BWB?BBB", ["B"]) == 87

def test_convert_condition_to_int_question():
    assert day12.convert_condition_to_int("BWB?BBB", ["B","?"]) == 95

def test_has_correct_number_of_broken_pumps():
    assert day12.has_correct_number_of_broken_pumps("BWBWBBB",5) == True

def test_has_correct_number_of_broken_pumps_false():
    assert day12.has_correct_number_of_broken_pumps("BBBWBBB",5) == False

def test_convert_int_to_condition():
    assert day12.convert_int_to_condition(87,7) == "BWBWBBB"

def test_get_all_possible_conditions():
    assert len(day12.get_all_possible_conditions("???WBBB",[1,1,3])) == 3
    assert day12.get_all_possible_conditions("???WBBB",[1,1,3]) == ["WBBWBBB","BWBWBBB", "BBWWBBB"]

def test_count_valid_combinations():
    combinations = day12.get_all_possible_conditions("????WBBBBBBWWBBBBB.",[1,6,5])
    assert day12.count_valid_combinations(combinations,[1,6,5]) == 4