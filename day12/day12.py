import sys
import re
from collections import Counter

sys.path.append( '../python_modules' )
import advent

def process_input(data, run_type) -> int:
    
    answer = 0
    for line in data:
        damaged_condition = get_conditions(line)
        size_of_groups = (get_size_of_groups(line))
        combos = get_all_possible_conditions(damaged_condition,size_of_groups)
        answer += count_valid_combinations(combos, size_of_groups)
    
    return answer


def get_conditions(line) -> str:
    end = line.find(" ")
    return line[:end].replace(".","W").replace("#","B")

def get_size_of_groups(line) -> list[int]:
    start = line.find(" ") + 1
    numbers_x= line[start:].split(",")
    return list(map(int, numbers_x))

def build_match_pattern(numbers: list[int]) -> str:
    not_first = False
    pattern = ""
    for num in numbers:
        if not_first:
            pattern += 'W+'
        not_first = True
        pattern  += "B" * num
    return pattern

def is_possible_match(test: str, pattern: str)->  bool:
    return re.search(pattern,test) != None

def convert_condition_to_int(condition: str, match) -> int:
    length = len(condition)
    ret_val = 0
    for idx,chr in enumerate(condition):
        if chr in match:
            ret_val += pow(2,length-idx-1)
    return ret_val

def has_correct_number_of_broken_pumps(condition: str, broken_count: int) -> bool:
    return Counter(condition)["B"] == broken_count

def convert_int_to_condition(number: int, length: int) -> str:
    bin_string =   '{0:b}'.format(number).zfill(length  )
    return bin_string.replace("0","W").replace("1","B")

def get_all_possible_conditions(incomplete_condition: str, numbers: list[int]) -> list[str]:
    ret_val = []
    broken_number = sum(numbers)
    length_of_condition = len(incomplete_condition)
    and_int_value = convert_condition_to_int(incomplete_condition, ["B"])
    or_int_value = convert_condition_to_int(incomplete_condition, ["B", "?"])

    max_value = pow(2,length_of_condition)
    for i in range(and_int_value, max_value):
        if (i & and_int_value  == and_int_value) and (i | or_int_value == or_int_value): # must match original pattern
            condition = convert_int_to_condition(i, length_of_condition)
            if has_correct_number_of_broken_pumps(condition, broken_number):
                ret_val.append(condition)
            
    return ret_val

def count_valid_combinations(conditions: list[str], numbers: list[int]) -> int:
    count = 0
    test = build_match_pattern(numbers)
    for condition in conditions:
        if is_possible_match(condition,test):
            count +=1
    return count

if __name__ == '__main__':
    if not advent.is_args_valid(sys.argv):
        print("Unrecoverable error - terminating program")
        sys.exit()

    data = advent.read_input(sys.argv[2])
    answer = process_input(data, sys.argv[1])
    print(f"Answer : {answer}")
