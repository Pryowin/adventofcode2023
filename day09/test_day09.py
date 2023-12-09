import day09

def test_get_oasis():
    arr = ["-7 -13 -20 -17 16",
           "0 3 6 9 12 15"
           ]
    assert day09.get_oasis(arr) == [[-7,-13,-20,-17,16],[0,3,6,9,12,15]]

def test_get_differences():
    assert day09.get_differences([0, 3, 6, 9, 12, 15,]) == [3, 3, 3, 3, 3]

def test_is_all_zero():
    assert day09.is_all_zero([0, 0, 0, 0]) == True

def test_is_all_zero_not():
    assert day09.is_all_zero([3, 3, 3, 3, 3]) == False

def test_get_sequences():
    assert day09.get_sequences([0, 3, 6, 9, 12, 15]) == [[0, 3, 6, 9, 12, 15],
                                                        [3, 3, 3, 3, 3],
                                                        [0, 0, 0, 0]]
    
def test_make_predictions():
    seq = day09.get_sequences([0, 3, 6, 9, 12, 15])
    assert day09.make_predictions(seq,"A") == 18

def test_make_predictions_b():
    seq = day09.get_sequences([10,13,16,21,30,45])
    assert day09.make_predictions(seq,"B") == 5