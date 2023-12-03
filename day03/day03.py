import sys

def read_input(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
    return data 

def process_input(data):

    answer = 0
    if RATIO:
        product_array = [[0] * len(data) for i in range(len(data[0]))]
        temp_array = [[0] * len(data) for i in range(len(data[0]))]

    for idx,line in enumerate(data):
        number_str = ""
        for pos,char in enumerate(line):
            if char.isdigit():
                if number_str == "":
                    start = pos
                number_str += char
            else:
                if number_str != "":
                    if RATIO:
                        process_number(number_str, data, idx, start, product_array, temp_array)
                    else:
                        answer += check_part_number(number_str, data, idx, start)
                    number_str = ""

        if number_str != "":
            if RATIO:
                process_number(number_str, data, idx, start, product_array, temp_array)
            else:
                answer += check_part_number(number_str, data, idx, start)
            
    if RATIO:
        answer = sum_products(product_array)
    print(f"Answer : {answer}")

def check_part_number(number_str, data, idx, start):

    num_len = len(number_str)
    if idx !=0: 
        if check_line_for_symbols(data[idx-1].rstrip(), start, num_len):
            return int(number_str)
    if idx < len(data) -1:
        if check_line_for_symbols(data[idx + 1].rstrip(), start, num_len):
            return int(number_str)
    if check_for_before_and_after_symbols(data[idx].rstrip(), start, num_len):
        return int(number_str)
    return 0 


def check_line_for_symbols(line, start, num_len) -> bool:
    for i in range(start, start + num_len):
        if is_symbol(line[i]):
            return True
    if check_for_before_and_after_symbols(line, start, num_len):
        return True
    return False

def check_for_before_and_after_symbols(line, start, num_len) -> bool:
    if start > 0:
        if is_symbol(line[start-1]) :
            return True
    if start + num_len < len(line) :
        if is_symbol(line[start + num_len]):
            return True
    return False

def is_symbol(char) -> bool:
    if char == "." or char.isdigit():
        return False
    else:
        return True

def process_number(number_str, data, idx, start, product_array, temp_array):
    num_len = len(number_str)
    if idx !=0: 
        check_line_for_multiply(int(number_str),data[idx-1].rstrip(),idx-1, start, num_len,product_array, temp_array)
    if idx < len(data) -1:
        check_line_for_multiply(int(number_str),data[idx + 1].rstrip(), idx+1, start, num_len,product_array, temp_array)
    check_for_before_and_after_multiply(int(number_str),data[idx].rstrip(), idx, start, num_len, product_array, temp_array)

def update_array(x,y, num, product_array,temp_array):
    val =  temp_array[x][y]
    if val == 0:
        temp_array[x][y] = num
    else:
        product_array[x][y] = temp_array[x][y] * num


def check_line_for_multiply(num, line, idx, start, num_len,product_array,temp_array): 
    for i in range(start, start + num_len):
        if line[i] == MULTIPY:
            update_array(idx,i,num,product_array,temp_array)
    check_for_before_and_after_multiply(num, line, idx, start, num_len,product_array,temp_array)
    
def check_for_before_and_after_multiply(num, line, idx, start, num_len,product_array,temp_array):
    if start > 0:
        if (line[start-1]) == MULTIPY:
            update_array(idx,start-1,num, product_array,temp_array)
            
            
    if start + num_len < len(line) :
        if (line[start + num_len]) == MULTIPY:
            update_array(idx,start + num_len,num, product_array,temp_array)

def sum_products(product_array) -> int:
    answer = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            answer += product_array[j][i]
    return answer


if sys.argv[1] == "A":
    RATIO = False
else:
    RATIO = True    

MULTIPY = "*"

data = read_input(sys.argv[2])
process_input(data)

