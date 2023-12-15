import day15

def test_convert_character_to_ascii():
    assert day15.convert_character_to_ascii("H") == 72

def test_hash_string():
    assert day15.hash_string("HASH") == 52

def test_get_hash_total():
    assert day15.get_hash_total("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7") == 1320

def test_remove_lens():
    boxes = [["rn","cm"], [], [],["pc", "ot", "ab"]],[[1, 2], [],[],[4,9,5]]
    response = day15.remove_lens(boxes, "pc")
    excepted_response = [["rn","cm"], [], [],["ot", "ab"]],[[1, 2], [],[],[9,5]]
    assert response ==  excepted_response
    
def test_add_lens():
    boxes = [["rn","cm"], [], [],["pc",  "ot"]],[[1, 2], [],[],[4,9]]
    excepted_response = [["rn","cm"], [], [],["pc", "ot", "ab"]],[[1, 2], [],[],[4,9,5]]
    assert day15.add_lens(boxes, "ab",5 ) == excepted_response

def test_replace_lens():
    boxes = [["rn","cm"], [], [],["pc", "ot", "ab"]],[[1, 2], [],[],[4,9,5]]
    excepted_response = [["rn","cm"], [], [],["pc", "ot", "ab"]],[[1, 2], [],[],[4,9,8]]
    assert day15.add_lens(boxes, "ab",8 ) == excepted_response

def test_get_focus_power():
    boxes =  [["rn","cm"], [], [],["pc", "ot", "ab"]],[[1, 2], [],[],[4,9,5]]
    assert day15.get_focus_power(boxes,0) == 5

def test_get_instruction_add():
    assert day15.get_instruction("qp=3") == ("qp", 3, True)

def test_get_instruction_remove():
    assert day15.get_instruction("cm-") == ("cm", 0, False)
