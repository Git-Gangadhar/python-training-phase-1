import random

print("Welcome to the game of rock, paper, scissors!")

while True:
    player1 = input("Player 1, please choose rock, paper, or scissors: ")
    player2 = input("Player 2, please choose rock, paper, or scissors: ")

    if player1 == player2:
        print("It's a tie!")
    elif player1 == "rock" and player2 == "scissors":
        print("Player 1 wins!")
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins!")
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    play_again = input("Do you want to play again? (yes/no) ")
    if play_again == "no":
        break
