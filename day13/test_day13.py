import day13
import sys

sys.path.append( '../python_modules' )
import advent

def test_is_mirror_image():
    assert day13.is_mirror_image("abc","cba")

def test_is_mirror_image_false():
    assert day13.is_mirror_image("abc","abc") == False

def test_split_line():
    assert day13.split_line("abcdef",3) == ("abc", "def")

def test_get_halfway_even():
    assert day13.get_halfway("abcdef") == 3

def test_get_halfway_odd():
    assert day13.get_halfway("abcdefg") == 4

def test_get_next_pattern():
    data = advent.read_input("test.txt")
    pattern = day13.get_next_pattern(data, 0)
    assert len(pattern) == 7
    assert pattern[6] == "#.#.##.#."
    next = len(pattern) + 1
    pattern2 = day13.get_next_pattern(data, next)
    assert len(pattern2) == 7
    assert pattern2[5] == "..##..###"

def test_check_all_for_mirror_image():
    assert day13.check_all_for_mirror_image(["abc", "123"],["cba", "321"])
    assert not day13.check_all_for_mirror_image(["abc", "123"],["cba", "421"])

def test_build_vertical_lines():
    lines = ["abc", "123","cba", "321"]
    assert day13.build_vertical_lines(lines) == ["a1c3","b2b2", "c3a1"]