from art import logo
from random import randint

#Global Constant to easily switch number of attempts available
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, answer, attempts):
    """
    Compares answer against user.
    Returns # of attempts remaining.
    :param user_guess:
    :param answer:
    :param attempts:
    :return:
    """
    if user_guess > answer:
        print("Too High.")
        #attempts -= 1 return is better
        return attempts - 1
    elif user_guess < answer:
        print("Too Low.")
        #attempts -= 1
        return attempts - 1
    else:
        print(f"You Win!! The answer was {answer}")

#Return the values as an output
#By setting it as return, we can call the funciton and use the output
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    """
    The global variables will become local by putting it inside game() function.
    """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")
    #global variable.. now local
    answer = randint(1, 100)
    print(f"TESTING: Correct answer is {answer}")

    #Calling this function will assign the output to attempts variable
    #global variable.. now local
    #this variable is updated below everytime answer is checked
    attempts = set_difficulty()

    #global variable.. now local
    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts left to guess the number.\n")
        guess = int(input("Make a guess: "))
        #Called to check answer, passing in input from user and answer output.
        #save number of turns remaining to variable attempts
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("\nYou are out of guesses. YOU LOSE.")
            #We are inside a function.
            #We will return and end here.
            return
        elif guess != answer:
            print("Guess again.")


#Call game() in global scope.
game()
