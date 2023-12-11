import sys

sys.path.append( '../python_modules' )
import advent

def process_input(data, run_type) -> int:
    inserted_rows = insert_rows(data)
    inserted_columns = insert_columns(data)
    galaxies = get_galaxies(data,inserted_rows,inserted_columns,run_type)
    answer = sum_shortest_paths(galaxies)
    return answer


def insert_rows(data) -> list[int]:
    ret_val = []
    for idx, line in enumerate(data):
        if line.find("#") == -1:
            ret_val.append(idx)
            
    return ret_val

def insert_columns(data) -> list[int]:
    empty_columns = []
    for idx in range(0,len(data[0])): 
        empty =  True
        for line in data:
            if line[idx] != ".":
                empty = False
                break
        if empty:
            empty_columns.append(idx)
            
    
    return empty_columns

def get_galaxies(data,inserted_rows, inserted_columns,run_type) -> list[tuple[int,int]]:
    galaxies = []
    
    if run_type == "A":
        expansion = 1
    else:
        expansion = 999999

    for y , line in enumerate(data):
        for x, chr in enumerate(line):
            if chr == "#":
                x1 = x + adjust_for_expansion(x,inserted_columns) * expansion
                y1 = y + adjust_for_expansion(y,inserted_rows) * expansion
                galaxies.append((x1,y1))
    return galaxies

def adjust_for_expansion(galaxy_line, inserted_lines) -> int:
    ret_val = 0
    for line in inserted_lines:
        if line < galaxy_line:
            ret_val += 1
        else:
            break
   
    return ret_val
    

def calc_distance(galaxy_one, galaxy_two) -> int:
    return abs(galaxy_one[0] - galaxy_two[0]) + abs(galaxy_one[1] - galaxy_two[1])

def sum_shortest_paths(galaxies) -> int:
    answer = 0
    for idx, galaxy in enumerate(galaxies):
        for pair_no in range(idx+1,len(galaxies)):
            answer += calc_distance(galaxy,galaxies[pair_no])
    return answer


if __name__ == '__main__':
    if not advent.is_args_valid(sys.argv):
        print("Unrecoverable error - terminating program")
        sys.exit()

    data = advent.read_input(sys.argv[2])
    answer = process_input(data, sys.argv[1])
    print(f"Answer : {answer}")
