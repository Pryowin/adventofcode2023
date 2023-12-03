import sys

def read_input(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
    return data 

def process_input(data):
    answer = 0
    for idx,line in enumerate(data):
        number_str = ""
        for pos,char in enumerate(line):
            if char.isdigit():
                if number_str == "":
                    start = pos
                number_str += char
            else:
                if number_str != "":
                    answer += check_part_number(number_str, data, idx, start)
                    number_str = ""

        if number_str != "":
            answer += check_part_number(number_str, data, idx, start)

    print(f"Answer : {answer}")

def check_part_number(number_str, data, idx, start):

    num_len = len(number_str)
    if idx !=0: 
        if check_line_for_symbols(data[idx-1].rstrip(), start, num_len):
            return int(number_str)
    if idx < len(data) -1:
        if check_line_for_symbols(data[idx + 1].rstrip(), start, num_len):
            return int(number_str)
    if check_for_before_and_after_symbols(data[idx].rstrip(), start, num_len):
        return int(number_str)
    return 0 


def check_line_for_symbols(line, start, num_len) -> bool:
    for i in range(start, start + num_len):
        if is_symbol(line[i]):
            return True
    if check_for_before_and_after_symbols(line, start, num_len):
        return True
    return False

def check_for_before_and_after_symbols(line, start, num_len) -> bool:
    if start > 0:
        if is_symbol(line[start-1]) :
            return True
    if start + num_len < len(line) :
        if is_symbol(line[start + num_len]):
            return True
    return False

def is_symbol(char) -> bool:
    if char == "." or char.isdigit():
        return False
    else:
        return True


data = read_input(sys.argv[2])
process_input(data)
