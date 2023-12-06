from os.path import exists

def read_input(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
    return data 

def is_args_valid(params) -> bool:
    if len(params) < 3:
        print("Must specify run type and input file")
        return False
    if "AB".find(params[1]) < 0:
        print("First parameter is the run type and must be 'A' or 'B")
        return False
    if not exists(params[2]):
        print(f"File {params[2]} does not exist")
        return False
    
    return True

# takes a string of data (line), a start position, and an optional separator
# returns an array of integers

def get_numbers(line,start, separator = " "):
    ret_array = []
    line = line[start:].strip()
    
    while line.find(separator) > 0:
        end=line.find(separator)
        ret_array.append(int(line[:end]))
        line=line[end+1:].strip()
    
    ret_array.append(int(line))
    return ret_array
