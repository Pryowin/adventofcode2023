import sys

sys.path.append( '../python_modules' )
import advent

def process_input(data, run_type) -> int:
    times = get_data(data[0])
    distances = get_data(data[1])
    return process_each_race(times, distances, run_type)

def get_data(line):
    ret_array = []
    start = line.find(":")+1
    line = line[start:].strip()
    while line.find(" ") > 0:
        end=line.find(" ")
        ret_array.append(int(line[:end]))
        line=line[end:].strip()
    ret_array.append(int(line))
    return ret_array

def process_each_race(times, distances, run_type):
    answer = 1
    for i in range(0,len(times)):
        answer = answer * winning_options(times[i],distances[i],run_type)
    return answer

def winning_options(time_of_race,best_distance,run_type):
    answer = 0
    for time_held_down in range(0,time_of_race):
        if travel_distance(time_of_race,time_held_down) > best_distance:
            answer += 1
    return answer
        
def travel_distance(time_of_race, time_held_down):
    speed = time_held_down
    distance = speed * (time_of_race - time_held_down)
    return distance 


if __name__ == '__main__':
    if not advent.is_args_valid(sys.argv):
        print("Unrecoverable error - terminating program")
        sys.exit()

    data = advent.read_input(sys.argv[2])
    answer = process_input(data, sys.argv[1])
    print(f"Answer : {answer}")
