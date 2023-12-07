import day07

def test_convert_values():
    assert day07.convert_values("AKQJT92") == "14131211100902"

def test_make_hand_dict():
    assert day07.make_hand_dict("K2KTT") == {"2":1, "K":2,"T":2}

def test_score_hand_5_of_a_kind():
    dict = day07.make_hand_dict("33333")
    assert day07.score_hand(dict) == 6

def test_score_hand_4_of_a_kind():
    dict = day07.make_hand_dict("TT3TT")
    assert day07.score_hand(dict) == 5

def test_score_hand_3_of_a_kind():
    dict = day07.make_hand_dict("KAKQK")
    assert day07.score_hand(dict) == 3

def test_score_hand_full_house():
    dict = day07.make_hand_dict("A333A")
    assert day07.score_hand(dict) == 4

def test_score_hand_two_pairs():
    dict = day07.make_hand_dict("334K4")
    assert day07.score_hand(dict) == 2

def test_score_hand_one_pair():
    dict = day07.make_hand_dict("AQ4K4")
    assert day07.score_hand(dict) == 1

def test_score_hand_high_card():
    dict = day07.make_hand_dict("324K8")
    assert day07.score_hand(dict) == 0

def test_get_hand():
    assert day07.get_hand("32T3K 765") == "32T3K"

def test_get_bid():
    assert day07.get_bid("32T3K 765") == 765


                        