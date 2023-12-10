import sys

sys.path.append( '../python_modules' )
import advent

DIRECTIONS = ((-1,0),(1,0),(0,-1),(0,1))

def process_input(data, run_type) -> int:
    map = create_field(data)
    set_max_dimensions(map)
    start = find_start()
    start_pipes = find_connected_pipes(start)
    answer = walk_pipes(start_pipes,start)
    return answer


def create_field(data) -> list[list[int]]:
    retval = []
    for line in data:
        line_list = []
        for chr in line:
            line_list.append(chr)
        retval.append(line_list)
    return retval

def get_contents(x, y) -> str:
    return field[y][x]

def set_max_dimensions(map):
    global max_x, max_y,field
    field = map
    max_x = len(field[0])
    max_y = len(field)



def get_pipe_ends(location, pipe) -> tuple[tuple[int,int],tuple[int,int]]:
    x = location[0]
    y = location[1]
    match pipe:
        case "|":
            return ((x,y+1),(x,y-1))
        case "-":
            return((x+1,y),(x-1,y))
        case "L":
            return((x+1,y),(x,y-1))
        case "J":
            return((x-1,y),(x,y-1))
        case "7":
            return((x-1,y),(x,y+1))
        case "F":
            return((x+1,y),(x,y+1))
        case _:
            return((x,y),(x,y))
        
def find_start() -> tuple[int,int]:

    for y in range(0,len(field)):
        for x in range(0,len(field[0])):
            if get_contents(x, y) == "S":
                return (x,y)
    raise Exception("No creature found")

def is_valid_direction(location,direction) -> bool:
    if location[0] == 0 and direction[0] == -1:
        return False
    if location[1] == 0 and direction[1] == -1:
        return False
    if location[0] + direction[0] >= max_x:
        return False
    if location[1] + direction[1] >= max_y:
        return False
    return True


def find_connected_pipes(start) -> tuple[tuple[int,int],tuple[int,int]]:
    found = False
    for direction in DIRECTIONS:
        if is_valid_direction(start, direction):
            check_location = (start[0] + direction[0], start[1] + direction[1])
            pipe = get_contents(check_location[0],check_location[1]) 
            ends = get_pipe_ends(check_location, pipe) 
            # print(f"Location {check_location} has {pipe} with {ends}")
            for i in range(0,2): 
                if ends[i] == start:
                    if found:
                        b = check_location
                    else:
                        a = check_location
                        found = True

    return (a,b)

def walk_pipes(start_pipes,start) -> int:
    moves = 0
    visited = set()
    route_one = start_pipes[0]
    route_two = start_pipes[1]
    start_one = start
    start_two = start
    while (not route_one in visited) or (not route_two in visited):
        visited.add(route_one)
        visited.add(route_two)
        moves += 1
        route_one_tmp = move_through_pipe(route_one,start_one)
        route_two_tmp = move_through_pipe(route_two,start_two)
        start_one = route_one
        start_two = route_two
        route_one = route_one_tmp
        route_two = route_two_tmp
    
    return moves

def move_through_pipe(pipe_location, start) -> tuple[int,int]:
    pipe = get_contents(pipe_location[0], pipe_location[1])
    ends = get_pipe_ends(pipe_location,pipe)
    if ends[0] == start:
        return ends[1]
    else:
        return ends[0]
    

if __name__ == '__main__':
    if not advent.is_args_valid(sys.argv):
        print("Unrecoverable error - terminating program")
        sys.exit()

    data = advent.read_input(sys.argv[2])
    answer = process_input(data, sys.argv[1])
    print(f"Answer : {answer}")
