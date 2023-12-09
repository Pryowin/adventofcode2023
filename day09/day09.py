import sys

sys.path.append( '../python_modules' )
import advent

def process_input(data, run_type) -> int:
    oasis = get_oasis(data)
    answer = 0
    for list in oasis:
        answer += make_predictions(get_sequences(list),run_type)
    
    return answer

def get_oasis(data):
    ret_val =[]
    for line in data:
        ret_val.append(advent.get_numbers(line,0))
    return ret_val

def get_differences(num_list):
    ret_val = []
    for i in range(1,len(num_list)):
        ret_val.append(num_list[i]-num_list[i-1])
    return ret_val

def is_all_zero(num_list):
    return num_list == [0] * len(num_list)

def get_sequences(num_list):
    sequences = []
    idx = 0
    sequences.append(num_list)
    while not is_all_zero(sequences[idx]):
        sequences.append(get_differences(sequences[idx]))
        idx +=1
    
    return sequences

def make_predictions(num_list,run_type) -> int:
    idx = len(num_list)
    num = 0
    while idx > 0:
        idx -= 1
        if run_type == "A":
            num += num_list[idx][-1]
        else:
            num = num_list[idx][0] - num
            
    return num 

if __name__ == '__main__':
    if not advent.is_args_valid(sys.argv):
        print("Unrecoverable error - terminating program")
        sys.exit()

    data = advent.read_input(sys.argv[2])
    answer = process_input(data, sys.argv[1])
    print(f"Answer : {answer}")
