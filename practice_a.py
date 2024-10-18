"""
A

Create a set of code that completes the following requirements:


The system should select a random number between 0-100.



The user should be able to guess four times, before revealing the answer.



The system should tell you if the guess is higher or lower than the actual number.,



Reminder: Insert comments, both a multi-line before the code and in-line comments.
"""

from random import randint

number = randint(0,100)
attempts = 1

print("")
guess = int(input("Guess a number from 0-100: "))
print("")

while attempts <= 4:
    if guess == number:
        print("Correct!")
        break
    else:
        if guess > number:
            print("The answer is lower")
            print("")
        else:
            print("The answer is higher")
            print("")
        guess = int(input("Your guess was incorrect, try again: "))
        print("")
        attempts += 1
        
    if attempts == 4:
        print(f"You are out of tries, the answer is {number}")
        
    