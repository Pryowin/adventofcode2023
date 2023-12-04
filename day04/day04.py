import sys


def read_input(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
    return data 

def process_input(data, runt_type) -> int:
    answer = 0
    game = 0
    for line in data:
        game += 1
        winning_numbers = get_winning_numbers(line)
        score = get_score(line, winning_numbers)
        print(f"Game {game}: {score}")
        answer += score
    return answer

def get_winning_numbers(line) -> list:
    winning_numbers = []
    start = line.find(":") + 2
    while line[start] != "|":
        num = int(line[start:start+2])
        winning_numbers.append(num)
        start  += 3
    return winning_numbers

def get_numbers(line) -> list:
    start = line.find("|") + 2
    iterations = int(len(line[start:])/3)
    numbers = []
    for i in range(0,iterations):
        num = int(line[start:start+2])
        numbers.append(num)
        start  += 3
    return numbers

def get_score(line, winning_numbers) -> int:
    score = 0
    numbers = get_numbers(line)
    for num in numbers:
        if num in winning_numbers:
            if score == 0:
                score = 1
            else:
                score = score * 2
    return score
    

data = read_input(sys.argv[2])
answer = process_input(data, sys.argv[1])
print(f"Answer : {answer}")

