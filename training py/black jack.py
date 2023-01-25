import random

# list of card values
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] 

# function to calculate total value of player's hand
def hand_value(hand):
    total = 0
    aces = 0
    for card in hand:
        if card == 11:
            aces += 1
        total += card
    # check for aces and adjust value if necessary
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

# function to play a round of Blackjack
def play_round():
    player_hand = []
    dealer_hand = []
    # initial deal
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    print("Your hand: ", player_hand, " (total: ", hand_value(player_hand), ")")
    print("Dealer's hand: ", dealer_hand[0], " and [hidden]")
    # player's turn
    while True:
        decision = input("Do you want to hit or stand? ")
        if decision == "hit":
            player_hand.append(random.choice(cards))
            print("Your hand: ", player_hand, " (total: ", hand_value(player_hand), ")")
            if hand_value(player_hand) > 21:
                print("You bust! Dealer wins.")
                return
        elif decision == "stand":
            break
    # dealer's turn
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(random.choice(cards))
    print("Dealer's hand: ", dealer_hand, " (total: ", hand_value(dealer_hand), ")")
    if hand_value(dealer_hand) > 21:
        print("Dealer busts! You win.")
    elif hand_value(dealer_hand) > hand_value(player_hand):
        print("Dealer wins.")
    elif hand_value(dealer_hand) < hand_value(player_hand):
        print("You win!")
    else:
        print("It's a tie!")

# play game
play_round()
