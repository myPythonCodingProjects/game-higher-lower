from art import logo, vs
from game_data import data
import random


def ask_user(a, b):
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}")
    return input("Who has more followers? Type 'A' or 'B' : ").title()


def compare(a_followers, b_followers, answer):
    if a_followers >= b_followers:
        return answer == 'A'
    else:
        return answer == 'B'


def play_game():
    print(logo)
    score = 0
    b = random.choice(data)
    while True:
        a = b
        while b == a:
            b = random.choice(data)
        answer = ask_user(a, b)
        print(logo)
        if compare(a['follower_count'], b['follower_count'], answer):
            score += 1
            print(f"You're right! Current Score, {score}")
        else:
            print(f"Sorry, that's wrong. Final Score, {score}")
            return


play_game()
