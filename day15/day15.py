import sys

sys.path.append( '../python_modules' )
import advent

FACTOR = 17
DIVISOR = 256

LABEL = 0
FOCAL_LENGTH = 1
IS_ADD = 2

def process_input(data, run_type) -> int:
    if run_type == "A":
        answer = get_hash_total(data[0])
    else:
        boxes = slot_boxes(data[0])
        answer = sum_focus_power(boxes)
        
    return answer

def convert_character_to_ascii(char) -> int:
    return ord(char)

def hash_string(string) -> int:
    hash_value = 0
    for char in string:
        ascii = convert_character_to_ascii(char)
        hash_value += ascii
        hash_value *= FACTOR
        hash_value = hash_value % DIVISOR
    
    return hash_value

def get_hash_total(line) -> int:
    strings = line.rstrip().split(",")
    total = 0
    for string in strings:
        total += hash_string(string)
    return total

def slot_boxes(line) -> list[list[str],list[int]]:
    boxes = [[[] for j in range(256)] for i in range(2)]
    strings = line.rstrip().split(",")
    for string in strings:
        instruction = get_instruction(string)
        if instruction[IS_ADD]:
            boxes = add_lens(boxes, instruction[LABEL], instruction[FOCAL_LENGTH])
        else:
            boxes = remove_lens(boxes, instruction[LABEL])

    return boxes

def sum_focus_power(boxes) -> int:
    power = 0
    for box_number, box in enumerate(boxes[1]):
        focus = get_focus_power(boxes, box_number)
        power += focus
    return power 

def get_instruction(string) -> tuple[str, int, bool]:
    pos = string.find("-")
    if pos > -1:
        label = string[:pos]
        focal = 0
        is_add = False
    else:
        pos = string.index("=")
        label = string[:pos]
        focal = int(string[pos+1])
        is_add = True
    return (label,focal, is_add)

    

def remove_lens(boxes, label) -> list[list[str],list[int]]:
    hash = hash_string(label)
    box = boxes[0][hash]
    box_fl = boxes[1][hash]
    try:
        position = box.index(label)
        box.pop(position)
        box_fl.pop(position)
        return boxes
    except:
        return boxes
    
def add_lens(boxes, label, focal_length) -> list[list[str],list[int]]:
    hash = hash_string(label)
    
    box = boxes[0][hash]
    box_fl = boxes[1][hash]
    try: 
        position = box.index(label)
        box[position] = label
        box_fl[position] = focal_length
        return boxes
    except:
        boxes[0][hash].append(label)
        boxes[1][hash].append(focal_length)
        return boxes

def get_focus_power(boxes, box_number) -> int:
    box = boxes[1][box_number]
    focus = 0
    for slot, lens in enumerate(box):
        focus += (box_number + 1) * (slot + 1) * lens
        
    return focus

if __name__ == '__main__':
    if not advent.is_args_valid(sys.argv):
        print("Unrecoverable error - terminating program")
        sys.exit()

    data = advent.read_input(sys.argv[2])
    answer = process_input(data, sys.argv[1])
    print(f"Answer : {answer}")
