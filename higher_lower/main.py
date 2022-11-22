from art import logo, vs
from game_data import data
import os
import random


def account_detail(account):
    """function for different dictionary value"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"compare a: {account_name}, {account_description}, from {account_country}."


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
lives = 0
on = True
account_b = random.choice(data)
while on:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"compare a: {account_detail(account_a)} ")
    print(vs)
    print(f"against b: {account_detail(account_b)} ")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]
    is_correct = check_answer(user_choice, a_follower, b_follower)

    os.system("clear")
    print(logo)

    if is_correct:
        lives += 1
        print(f"you win, your score is {lives}")
    else:
        on = False
        print(f"you lose, your score is {lives}")
