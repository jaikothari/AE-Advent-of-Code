'''
This is a solution attempt for week 7 advent of code problem.
The detailed problem can be found here - https://adventofcode.com/2023/day/7
The solution assumes the example is in a nested list form and appends type and rank to it to compute the final winning count.
'''

# Get the type of hand as a number representation for easy sorting
def get_type(hand):
    cards = sorted(hand)
    length = len(set(cards))
    counts = [cards.count(card) for card in set(cards)]
    
    if length == 2:
        # Four of a kind or Full house
        if 4 in counts:
            return(7)  # Four of a kind
        elif 3 in counts and 2 in counts:
            return(6)  # Full house
    elif length == 3:
        # Three of a kind or Two pair
        if 3 in counts:
            return(3)  # Three of a kind
        elif 2 in counts:
            return(2)  # Two pair
    elif length == 4:
        return(1)  # One pair
    elif length == 5:
        # Check for straight or high card
        values = "23456789TJQKA"
        if "".join(cards) in values:
            return(5)  # Straight
        return(4)  # High card

# Get the rank of the hands based on the type and priority of the individual cards
def get_rank(hands_with_bids):
    hands_with_bids.sort(key = lambda x: (x[2], -x[1]))
    count = 1
    for hand_with_bid in hands_with_bids:
        hand_with_bid.append(count)
        count += 1
    return(hands_with_bids)

# Calculate the final total winnings for all the hands
def calculate_winnings(hands_with_bids):
    total_winnings = 0
    for hand_with_bid in hands_with_bids:
        hand_with_bid.append(get_type(hand_with_bid[0]))
    hands_with_bids = get_rank(hands_with_bids)
    for hand_with_bid in hands_with_bids:
        total_winnings += hand_with_bid[1] * hand_with_bid[3]
    return(total_winnings)

# Main function definition with example
def main():
    hands_with_bids = [
        ["32T3K", 765],
        ["T55J5", 684],
        ["KK677", 28],
        ["KTJJT", 220],
        ["QQQJA", 483],
    ]
    total_winnings = calculate_winnings(hands_with_bids)
    print(f"Total Winnings: {total_winnings}")

# Name main idiom
if __name__ == "__main__":
    main()
