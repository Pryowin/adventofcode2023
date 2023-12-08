import sys
import math
from functools import reduce

sys.path.append( '../python_modules' )
import advent

def process_input(data, run_type) -> int:
    instructions = get_instructions(data[0])
    location_dictionary = get_location_dict(data[2:])
    if run_type == "A":
        start = "AAA"
        destination = "ZZZ"
        answer = navigate(location_dictionary, instructions, start, destination)
    else:
        start_list = get_start_locations(location_dictionary)
        answer = ghost_move(location_dictionary,instructions, start_list)
    
    return answer

def get_start_locations(location_dictionary):
    return list(filter(lambda str: str[2] == "A", location_dictionary))

def count_destinations(location_dictionary) -> int:
    return len(list(filter(lambda str: str[2] == "Z", location_dictionary)))

def ghost_move(location_dictionary, instructions, start_list) -> int:
    
    ghost_number = len(start_list)
    moves_to_z = [0] * ghost_number
    instruction_count = len(instructions)
    for idx in range(0, len(start_list)):
        current_location = start_list[idx]
        moves = - 1
        while current_location[2] != "Z":
            moves +=1 
            instruction = instructions[moves % instruction_count]
            node = location_dictionary[current_location]
            current_location = get_next_node(node,instruction)
        
        moves_to_z[idx] = moves + 1


    return lcm(moves_to_z)
    
def lcm(arr):

    l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
    return l

def get_instructions(line):
    return list(line.strip())

def get_location(line):
    end = line.find(" = ")
    return line[0:end]

def get_left_right(line):
    start = line.find("(")
    end = line.find(")")
    text = line[start+1:end]
    return text.split(", ")

def get_location_dict(data):
    map_dict = {}
    for line in data:
        key = get_location(line)
        left_right = get_left_right(line)
        map_dict[key] = left_right

    return map_dict

def get_next_node(current_node, instruction):
    if instruction == "L":
        return current_node[0]
    else:
        return current_node[1]
    
def navigate(location_dictionary, instructions, start, destination) -> int:
    count = -1
    current_location = start
    instruction_count = len(instructions)

    while current_location != destination:
        count += 1
        instruction = instructions[count % instruction_count]        
        node = location_dictionary[current_location]
        current_location = get_next_node(node,instruction)
        

    return count + 1

if __name__ == '__main__':
    if not advent.is_args_valid(sys.argv):
        print("Unrecoverable error - terminating program")
        sys.exit()

    data = advent.read_input(sys.argv[2])
    answer = process_input(data, sys.argv[1])
    print(f"Answer : {answer}")
