import day07

def test_convert_values():
    assert day07.convert_values("AKQJT92") == "14131211100902"

def test_convert_values_B():
    assert day07.convert_values("AKQJT92",day07.CARD_VALUE_B) == "14131201100902"

def test_make_hand_dict():
    assert day07.make_hand_dict("K2KTT","A") == {"2":1, "K":2,"T":2}

def test_make_hand_dict_with_jokers():
    assert day07.make_hand_dict("KJKTT","B") == {"K":3,"T":2}

def test_make_hand_dict_with_no_jokers():
    assert day07.make_hand_dict("KKKTT","B") == {"K":3,"T":2}

def test_make_hand_dict_with_all_jokers():
    assert day07.make_hand_dict("JJJJJ","B") == {"J":5}

def test_score_hand_5_of_a_kind():
    dict = day07.make_hand_dict("33333","A")
    assert day07.score_hand(dict) == 6

def test_score_hand_4_of_a_kind():
    dict = day07.make_hand_dict("TT3TT","A")
    assert day07.score_hand(dict) == 5

def test_score_hand_3_of_a_kind():
    dict = day07.make_hand_dict("KAKQK","A")
    assert day07.score_hand(dict) == 3

def test_score_hand_full_house():
    dict = day07.make_hand_dict("A333A","A")
    assert day07.score_hand(dict) == 4

def test_score_hand_two_pairs():
    dict = day07.make_hand_dict("334K4","A")
    assert day07.score_hand(dict) == 2

def test_score_hand_one_pair():
    dict = day07.make_hand_dict("AQ4K4","A")
    assert day07.score_hand(dict) == 1

def test_score_hand_high_card():
    dict = day07.make_hand_dict("324K8","A")
    assert day07.score_hand(dict) == 0

def test_get_hand():
    assert day07.get_hand("32T3K 765") == "32T3K"

def test_get_bid():
    assert day07.get_bid("32T3K 765") == 765

def test_score_jokers_one_joker():
    assert day07.score_jokers({"K":2,"T":2},1) == {"K":3,"T":2}

def test_score_jokers():
    assert day07.score_jokers({"K":2,"T":1},2) == {"K":4,"T":1}
                        