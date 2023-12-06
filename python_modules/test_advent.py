import pytest
import advent

def test_is_args_valid_no_params(capsys):
    assert advent.is_args_valid([]) == False
    captured = capsys.readouterr()
    assert captured.out == "Must specify run type and input file\n"

def test_is_args_valid_all_params():
    assert advent.is_args_valid(["pgmname", "A", "test_advent.py"]) == True

def test_is_args_valid_wrong_type(capsys):
    assert advent.is_args_valid(["pgmname", "Z", "test_advent.py"]) == False
    assert capsys.readouterr().out == "First parameter is the run type and must be 'A' or 'B\n"

def test_is_args_valid_missing_file(capsys):
    assert advent.is_args_valid(["pgmname", "B", "missing.py"]) == False
    assert capsys.readouterr().out == "File missing.py does not exist\n"

def test_get_numbers_default_separator():
    assert advent.get_numbers("Time:      7  15   30",5) == [7,15,30]

def test_get_numbers_comma_separator():
    assert advent.get_numbers("Time:      7,15,30",5,",") == [7,15,30]
