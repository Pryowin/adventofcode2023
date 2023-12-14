ROCK = 1
CUBE = 0
SPACE = -1

import sys
import copy

sys.path.append( '../python_modules' )
import advent


def process_input(data, run_type) -> int:
    grid = build_platform(data)
    new_grid = slide_rocks(grid)
    answer = score_grid(new_grid)

    return answer


def build_platform(data) -> list[list[int]]:
    ret_val = []
    for line in data:
        row = []
        for char in line.rstrip():
            match char:
                case "O":
                    row.append(ROCK)
                case "#":
                    row.append(CUBE)
                case _:
                    row.append(SPACE)
        ret_val.append(row)
    return ret_val

def get_contents(grid,x,y) -> int:
    return grid[y][x]

def display(grid):
    for line in grid:
        for num in line:
            print(convert_to_symbol(num),end='')
        print()

def convert_to_symbol(num):
    match num:
        case -1:
            return "."
        case 0:
            return "#"
        case 1:
            return "O"
        
    

def slide_rocks(grid: list[list[int]]) -> list[list[int]]:
    updated_grid = copy.deepcopy(grid)

    for x, columns in enumerate(updated_grid[0]):
        fall_to = 0
        for y, rows in enumerate(updated_grid):
            contents = get_contents(updated_grid,x,y)
            if contents == ROCK:
                if y != fall_to:
                    updated_grid[y][x] = SPACE
                    updated_grid[fall_to][x] = ROCK
                    fall_to = fall_to + 1
                else:
                    fall_to = y + 1

            if contents == CUBE:
                fall_to = y + 1
    
    return updated_grid

def not_negative(n) -> bool:
    return n >= 0

def score_grid(grid) -> int:
    score = 0

    for y, rows in enumerate(grid):
        weight = len(grid) - y
        score += sum(list(filter(not_negative, grid[y]))) * weight

    return score
             
if __name__ == '__main__':
    if not advent.is_args_valid(sys.argv):
        print("Unrecoverable error - terminating program")
        sys.exit()

    data = advent.read_input(sys.argv[2])
    answer = process_input(data, sys.argv[1])
    print(f"Answer : {answer}")
