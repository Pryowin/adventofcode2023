import sys

sys.path.append( '../python_modules' )
import advent

def process_input(data, run_type) -> int:
    with_inserted_rows = insert_rows(data)
    with_inserted_columns = insert_columns(with_inserted_rows)
    galaxies = get_galaxies(with_inserted_columns)
    answer = sum_shortest_paths(galaxies)
    return answer


def insert_rows(data) -> list[str]:
    ret_val = []
    for idx, line in enumerate(data):
        ret_val.append(line)
        if line.find("#") == -1:
            ret_val.append(line)
    return ret_val

def insert_columns(data) -> list[str]:
    empty_columns = []
    ret_val = []
    for idx in range(0,len(data[0])): 
        empty =  True
        for line in data:
            if line[idx] != ".":
                empty = False
                break
        if empty:
            empty_columns.append(idx)
    
    
    for line in data:
        added_columns = 0
        for expand in empty_columns:
            insert_at = expand + added_columns
            added_columns += 1
            line = line[:insert_at] + "." + line[insert_at:]
        ret_val.append(line)
    
    return ret_val

def get_galaxies(data) -> list[tuple[int,int]]:
    galaxies = []
    for y , line in enumerate(data):
        for x, chr in enumerate(line):
            if chr == "#":
                galaxies.append((x,y))
    return galaxies

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
