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
