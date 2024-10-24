"""
B.1 Create a python program that will allow a user to input a certain amount of change, and then print how many quarters, dimes, nickels, and pennies are needed to make up the amount needed.

B.2 Create a Mad Libs-style game, where the program asks the user for certain types of words, and then prints out a story with the words that the user input. The story doesn't have to be too long, but it should have some sort of storyline.
    - Output the resulting story into a text file

B.3 Create a game that will challenge you against the computer in a game of rock paper scissors. The user will input whether they choose rock paper or scissors and the computer will also choose one. The first to two will win the game
"""

# B.3

from random import randint

comp_choice = randint(1,3)

if comp_choice == 1:
    comp_choice = "rock"
elif comp_choice == 2:
    comp_choice = "paper"
elif comp_choice == 3:
    comp_choice = "scissors"

game = 0
comp_wins = 0
user_wins = 0
ties = 0

while True:
    game += 1
    print(f"Game {game}")
    print("Lets play rock, paper, scissors!\n")
    print("Options:\n1. Rock\n2. Paper\n3.Scissors")
    user_choice = int(input("Pick one(by number): "))

    if user_choice == 1:
        user_choice = "rock"
    elif user_choice == 2:
        user_choice = "paper"
    elif user_choice == 3:
        user_choice = "scissors"
    elif user_choice == 4:
        print(f"You won {user_wins} times and the computer won {comp_wins}.\nYou tied {ties} times.")
        if user_wins > comp_wins:
            print("You won the most")
        elif user_wins < comp_wins:
            print("The computer won the most")
        elif user_wins == comp_choice:
            print("You tied in wins")

        if ties > user_wins and ties > comp_wins:
            print("You tied the most")
        
        break

    print(f"{user_choice} v. {comp_choice}")

    if user_choice == comp_choice:
        print("Tie!")
        ties +=1
    elif user_choice == "rock" and comp_choice == "paper" or user_choice == "paper" and comp_choice == "scissors" or user_choice == "scissors" and comp_choice == "rock":
        print("CPU won")
        comp_wins +=1
    else:
        print("You won!")
        user_wins += 1