import sys
import copy

sys.path.append( '../python_modules' )
import advent

MAP = ["seed-to-soil", 
       "soil-to-fertilizer",
       "fertilizer-to-water", 
       "water-to-light", 
       "light-to-temperature", 
       "temperature-to-humidity",
       "humidity-to-location"]

def process_input(data,run_type) ->int:
    seeds = read_first_line(data[0])
    maps = read_other_lines(data[1:])
    answer = process_seeds_into_maps(seeds, maps)
    return answer

def read_first_line(line):
    seeds = []
    start = line.find(":") + 2
    line_remaining = line[start:]
    while line_remaining.find(" ") >=0 :
        end = line_remaining.find(" ")
        str = line_remaining[:end]
        seeds.append(int(str))  
        line_remaining = line_remaining[end+1:]
    seeds.append(int(line_remaining))

    return seeds

def read_other_lines(data):

    map = -1
    maps = []
    map_lines=[]
    map_line=[]
    for line in data:
        if line.rstrip() == "":
            continue

        if line.find("map:")>0:
            if map >=0:
                maps.append(copy.deepcopy(map_lines))
                del map_lines[:]
            map +=1
            continue

        line_remaining = line
        while line_remaining.find(" ") >=0 :
            end = line_remaining.find(" ")
            str = line_remaining[:end]
            map_line.append(int(str))  
            line_remaining = line_remaining[end+1:]

        map_line.append(int(line_remaining))
        
        map_lines.append(copy.deepcopy(map_line))
        del map_line[:]
    
    maps.append(copy.deepcopy(map_lines))
    return maps

def process_seeds_into_maps(seeds, maps):
    min_value = -1

    for seed in seeds:
        seed_loc = seed
        i= -1
        for locations in maps:
            i += 1
            for location in locations:
                if seed_loc >= location[1] and seed_loc < location[1] + location[2]:
                    from_loc = seed_loc
                    seed_loc = seed_loc - location[1] + location[0]
                   
                    break
        if min_value == -1 or seed_loc < min_value:
            min_value = seed_loc

    return min_value

    

if __name__ == '__main__':
    if not advent.is_args_valid(sys.argv):
        print("Unrecoverable error - terminating program")
        sys.exit()

    data = advent.read_input(sys.argv[2])
    answer = process_input(data, sys.argv[1])
    print(f"Answer : {answer}")

