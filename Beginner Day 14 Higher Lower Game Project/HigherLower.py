from art import logo, vs
from game_data import data
from replit import clear
import random


def format_data(account):
    """
    Takes the account data and returns the printable format. 
    """
    insta_name = account["name"]
    insta_descr = account["description"]
    insta_country = account["country"]
    return f"{insta_name}, a {insta_descr}, from {insta_country}"

def check_answer(guess, a_followers, b_followers):
    """
    Takes the user's guess, follower counts, and returns if they got it right.
    """
    # if a_followers > b_followers:
    #     if guess == "a":
    #         return True
    #     else:
    #         return False

    #BETTER ALTERNATIVE
    #When guess == "a" is evaluated, then it will return True
    #If guess is not "a", meaning "b", then reutrn False
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
 

#Display art
print(logo)
score = 0
continue_game = True
account_b = random.choice(data)



while continue_game:
    #Make account at position B become the next account at positon A. 
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"\nCompare A: {format_data(account_a)}")
    print(vs)
    print(f"\nAgainst B: {format_data(account_b)}")

    #Ask user for a guess
    user_guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    #Check if user is correct
    #Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    #Clear screen b/w rounds 
    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right. Current score: {score}")
    else:
        continue_game = False
        print(f"WRONG. Game over. Final Score: {score}")
        
