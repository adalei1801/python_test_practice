"""
A

Create a set of code that completes the following requirements:


The system should select a random number between 0-100.



The user should be able to guess four times, before revealing the answer.



The system should tell you if the guess is higher or lower than the actual number.,



Reminder: Insert comments, both a multi-line before the code and in-line comments.
"""

"""
This program allows a uer four guesses at a number before 0 and 100
"""

from random import randint
# Imports randint function from random module

number = randint(0,100)
# Assigns random number to variable
attempts = 1


print("")
guess = int(input("Guess a number from 0-100: "))
print("")
# Allows user to input a guess 

while attempts <= 4:
    # While loop that iterates through guesses
    if guess == number:
        print("Correct!")
        break
    # If statement that runs if user is correct and breaks the loop
    else:
        if guess > number:
            print("The answer is lower")
            # If statement that tells the user that their guess is too larger
        else:
            print("The answer is higher")
            # Else statement that tells the user their guess is below the number
        guess = int(input("Your guess was incorrect, try again: "))
        # Gives the user another guess as the loop iterates
        print("")
        attempts += 1
        # Increases attempt by one
        
    if attempts == 4:
        print(f"You are out of tries, the answer is {number}")
        break
    # If statement for the user running out of tries and breaks the loop
        
    