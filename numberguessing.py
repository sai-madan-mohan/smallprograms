import random

#Generate a random number between 1 and 100
number = random.randint(1,100)

#Ask the user for a guess
guess = int(input("Guess the number between 1 and 100 : "))

#check if the guess is correct
if guess == number:
    print("COngratulations You have guesses the correct number")
else:
    print(f"Sorry the number was{number}.Try again")
    