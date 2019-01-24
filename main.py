#Guess a number game!

import random

print("Welcome to 'Guess My Number'!")
name = input("\tWhat is your name? ")
print("Well," + name + "\nI'm thinking of a number between 1 and 20.")
print("Try to guess it in as few attempts as possible.\n")

# Class and method for checking guesses
class CheckGuess:
    def Call(self):
                    # Check guesses
                if guess == 5:
                    # User message
                    print("Sorry, you ran out of guesses... Better luck next time")
                    # Exit program
                    exit()
        
# Set Value for while loop
userPassed = 0
# Range of random
intRange = 20
# Declare random
answer = random.randint(1, 20)
# Declare Variable to hold guess count
guess = 0
# Open loop
while userPassed == 0:
    # Ask user for input
    userInput = input("Enter a number between 1 and {}: ".format(intRange))
    # Error handling
    try:
        # Convert string to integer
        userInput = int(userInput)
        # Check if input equals answer
        if userInput == answer:
            # Increment by 1
            guess = guess + 1
            # Congratulate user
            print("Well done!" + name + ", You guessed it!  The number was", answer)
            print("It only took you", guess, "tries! :)\n")
            # Increase value by 1, closes while loop
            userPassed = userPassed + 1
        # Check if input is greater than answer
        elif userInput > answer:
            # Increment by 1
            guess = guess + 1
            # Return message to user
            print("Your answer {} was too high, you have guessed {} times so far".format(userInput, guess))
            # Call method to check guess
            CG = CheckGuess()
            CG.Call()
        # Check if input is less than answer
        elif userInput < answer:
            # Increment by 1
            guess = guess + 1
            # Return message to user
            print("Your answer {} was too low, you have guessed {} times so far".format(userInput, guess))
            # Call method to check guess
            CG = CheckGuess()
            CG.Call()   
    except ValueError:
        # Increment by 1
        guess = guess + 1
        # Call method to check guess
        CG = CheckGuess()
        CG.Call()
        # Return message to user
        print("Please Enter a valid number")   
