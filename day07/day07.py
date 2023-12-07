import sys
import operator

sys.path.append( '../python_modules' )
import advent

CARD_VALUE = {
    "A": "14",
    "K": "13",
    "Q": "12",
    "J": "11",
    "T": "10"
}

SCORES = ["High Card","One Pair", "Two Pairs", "Three of a Kind", "Full House", "Four of a Kind", "Five of a Kind"]


class Hand:
    def __init__(self, hand, numeric_hand, bid, rank):
        self.hand = hand
        self.numeric_hand = numeric_hand
        self.bid = bid
        self.rank = rank


def process_input(data, run_type) -> int:
    hands = []
    for line in data:
        hand = get_hand(line)
        bid = get_bid(line)
        converted_hand = convert_values(hand)
        hand_dict = make_hand_dict(hand)
        rank  = score_hand(hand_dict)
        hands.append(Hand(hand, converted_hand,bid,rank))
    
    
    return score_hands(hands)

def get_hand(line) ->str:
    return line[0:5]

def get_bid(line) -> str:
    return int(line[6:])

def convert_values(hand) -> str:
    ret_val = ""
    for char in hand:
        if char in CARD_VALUE:
            ret_val += CARD_VALUE[char]
        else:
            ret_val += "0" + char
    return ret_val

def make_hand_dict(hand) -> dict:
    hand_check = {}
    for char in hand:
        if char in hand_check:
            hand_check[char] = hand_check[char] + 1
        else:
            hand_check[char] = 1
    return hand_check

def score_hand(hand_dict) -> int:
    is_five = False
    is_four = False
    is_three = False
    pairs = 0

    for entry in hand_dict.values():
        match entry:
            case 5:
                is_five = True
            case 4:
                is_four = True
            case 3:
                is_three = True
            case 2:
                pairs +=1
    
    if is_five:
        return 6 # Five of a kind
    if is_four:
        return 5 # Four of a kind
    if is_three and pairs == 1:
        return 4 # Full house
    if is_three:
        return 3 # Three of a kind
    if pairs == 2:
        return 2 # Two Pairs
    if pairs == 1:
        return 1 # One Pair
    return 0

def score_hands(hands) -> int:
    hands.sort(key = operator.attrgetter('rank','numeric_hand'))
    score = 0
    for i in range(0,len(hands)):
        score += hands[i].bid * (i+1)
    return score


if __name__ == '__main__':
    if not advent.is_args_valid(sys.argv):
        print("Unrecoverable error - terminating program")
        sys.exit()

    data = advent.read_input(sys.argv[2])
    answer = process_input(data, sys.argv[1])
    print(f"Answer : {answer}")
