from random import randint
from art import logo
l = randint(1, 100)

EASY_TURN = 4
HARD_TURN = 9
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(l)
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def turn_value():
    """condition part"""
    if level == "hard" or level == "h":
        return EASY_TURN
    elif level == "easy" or level == "e":
        return HARD_TURN
    else:
        print("wrong input")


on = True
value = turn_value()
while on:
    print(f"You have {value+1} attempts remaining to guess the number.")
    guess = int(input("guess your number: "))
    if guess == l:
        print(f"You won. correct number is {l}")
        on = False
    elif value == 0:
        print("You ran out of lives.")
        on = False

    elif guess < l:
        value -= 1
        print("Too low.")

    elif guess > l:
        value -= 1
        print("Too high.")

