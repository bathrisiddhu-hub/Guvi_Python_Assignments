# Write the code for Guess the Number using variables, conditions, loops
# Using import function to select random numbers with in a given range
import random
random_number = random.randint(1, 10)
player_guess = 0

while player_guess != random_number:
    player_guess = int(input("Guess the number: "))
    if player_guess > random_number:
        print("Too high")
    elif player_guess < random_number:
        print("Too low")
    else:
        print(f"Correct", {random_number})




