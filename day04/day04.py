import sys

sys.path.append( '../python_modules' )
import advent

def process_input(data, run_type) -> int:
    answer = 0
    game = -1
    if run_type == "B":
        scores = [0] * len(data)

    for line in data:
        game += 1
        winning_numbers = get_numbers(line, True)
        score = get_score(line, winning_numbers, run_type)
        if run_type == "A":
            answer += score
        else:
            scores[game] = score

    if run_type == "B":
        answer = process_scores(scores)

    return answer

def get_numbers(line, is_winning) -> list:

    numbers = []

    if is_winning:
        start = line.find(":") + 2
        end = line.find("|")
        iterations = int(len(line[start:end])/3)
    else:
        start = line.find("|") + 2
        iterations = int(len(line[start:])/3)

    for i in range(0,iterations):
        num = int(line[start:start+2])
        numbers.append(num)
        start  += 3
    return numbers

def get_score(line, winning_numbers, run_type) -> int:
    score = 0
    numbers = get_numbers(line,False)
    for num in numbers:
        if num in winning_numbers:
            if run_type == "A":
                if score == 0:
                    score = 1
                else:
                    score = score * 2
            else:
                score += 1

    return score
    
def process_scores(scores)->int:
    answer = len(scores)
    for card in range(0, len(scores)):
        answer += process_card(scores, card)
    return answer    

def process_card(scores, card)->int:
    
    answer = scores[card]
    if answer > 0:
        for i in range(card+1,card+1+answer):
            answer += process_card(scores, i)
    return answer
        
if not advent.is_args_valid(sys.argv):
    print("Unrecoverable error - terminating program")
    sys.exit()

data = advent.read_input(sys.argv[2])
answer = process_input(data, sys.argv[1])
print(f"Answer : {answer}")

