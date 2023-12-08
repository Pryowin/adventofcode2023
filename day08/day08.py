import sys

sys.path.append( '../python_modules' )
import advent

def process_input(data, run_type) -> int:
    instructions = get_instructions(data[0])
    location_dictionary = get_location_dict(data[2:])
    start = "AAA"
    destination = "ZZZ"

    return navigate(location_dictionary, instructions, start, destination, run_type)

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
    
def navigate(location_dictionary, instructions, start, destination, run_type) -> int:
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
