"""
B.1 Create a python program that will allow a user to input a certain amount of change, and then print how many quarters, dimes, nickels, and pennies are needed to make up the amount needed.

B.2 Create a Mad Libs-style game, where the program asks the user for certain types of words, and then prints out a story with the words that the user input. The story doesn't have to be too long, but it should have some sort of storyline.
    - Output the resulting story into a text file

B.3 Create a game that will challenge you against the computer in a game of rock paper scissors. The user will input whether they choose rock paper or scissors and the computer will also choose one. The first to two will win the game
"""

# B.1


def coin_count(change):
   change = change // .25
   print(change)
   change = change // .1
   print(change)
   

change = float(input("How much change do you have? "))
coin_count(change)

