import random
from art import logo
import os


def continue_game_agian():
    print(logo)

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        random_card = random.choice(cards)
        return random_card

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Opponent went over. You win 😁"
        elif user_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"

    user_cards = []
    computer_cards = []
    on = True
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while on:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(
            f"your first card is {user_cards} and current score {user_score}")
        print(f"computer first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            on = False
        else:
            pass_step = input("step y or pass n: ")
            if pass_step == "y":
                user_cards.append(deal_card())
            else:
                on = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"   Computer's final hand: {computer_cards}, final score: {computer_score}"
    )
    print(compare(user_score, computer_score))


while input("do you want to play blackjack y or n :") == "y":
    os.system("clear")
    continue_game_agian()
