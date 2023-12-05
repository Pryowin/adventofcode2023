import day05

def test_read_first_line():
    assert(day05.read_first_line("seeds: 79 14 55 13")) == [79,14,55,13]

def test_read_other_lines():
    input = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15"
    ]
    assert len(day05.read_other_lines(input[1:]))==2

def test_read_other_lines_makes_array_of_arrays():
    input = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15"
    ]
    assert day05.read_other_lines(input[1:])[1][0] == [0,15,37]

def test_get_seed_ranges():
    input = [5,3,20,2]
    assert len(day05.get_seed_ranges(input)) == 5
    assert day05.get_seed_ranges(input)[2] == 7
