import sys

sys.path.append( '../python_modules' )
import advent

def process_input(data, run_type) -> int:
    start = 0
    answer = 0
    while start <= len(data):
        lines = get_next_pattern(data, start)
        column = process_vertical_images(lines)
        row = process_horizontal_images(lines) 
        answer += column + row * 100
        start += len(lines) +1

    return answer

def process_vertical_images(lines) -> int:
    mirror_check = process_splits(lines)
    if mirror_check[1]:
        return mirror_check[0]
    else:
        return 0

def process_horizontal_images(lines) -> int:
    vertical_lines = build_vertical_lines(lines)
    mirror_check = process_splits(vertical_lines)
    if mirror_check[1]:
        return mirror_check[0]
    else:
        return 0
    
def build_vertical_lines(lines) -> list[str]:
    vertical_lines = []
    for i in range(0, len(lines[0])):
        line = ""
        for j in range(0, len(lines)):
            line += lines[j][i]
        vertical_lines.append(line)
    return vertical_lines

def is_mirror_image(text1: str, text2:str) -> int:
    return text1 == "".join(reversed(text2))

def split_line(line, split_point) -> tuple[str,str]:
    return(line[:split_point], line[split_point:])

def get_halfway(line) -> int:
    return round(len(line) / 2)

def get_next_pattern(data, start) -> list[str]:
    ret_val = []
    for line in data[start:]:
        if line.strip() == "":
            break
        ret_val.append(line.rstrip())
    return ret_val

def check_all_for_mirror_image(lefts, rights) -> bool:
    for idx, left in enumerate(lefts):
        right = rights[idx]
        truncated  = truncate_longer(left,right)
        if not is_mirror_image(truncated[0], truncated[1]):
            return False
    return True


def truncate_longer(left, right) -> tuple[str,str]:
    right_length = len(right)
    left_length = len(left)
    if left_length > right_length:
        return (left[left_length-right_length:],right)
    else:
        return (left,right[:left_length])

def process_splits(lines) -> tuple[int,bool]:
    is_image_found = False
    idx = 1
    count = 0
    while idx < len(lines[0]):
        lefts = []
        rights = []
        for line in lines:
            splits = split_line(line, idx)

            lefts.append(splits[0])
            rights.append(splits[1])
        if check_all_for_mirror_image(lefts,rights):
            is_image_found = True
            count += idx
            break
        else:
            idx +=1
    return (count,is_image_found)
            


if __name__ == '__main__':
    if not advent.is_args_valid(sys.argv):
        print("Unrecoverable error - terminating program")
        sys.exit()

    data = advent.read_input(sys.argv[2])
    answer = process_input(data, sys.argv[1])
    print(f"Answer : {answer}")
