rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Rock wins against scissors.    0 > 2
# Scissors wins against paper.   2 > 1
# Paper wins against rock.       1 > 0

# 0 is rock
# 1 is paper
# 2 is scissors

import random

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if user_choice >= 3 or user_choice < 0:
  print("Invalid number! Play again.\n")
else:
  print(game_images[user_choice])

  # Computer will choose from 0, 1, 2
  computer_choice = random.randint(0, 2)
  print(f"\nComputer chose: \n")
  print(game_images[computer_choice])
  
  if user_choice == 0 and computer_choice == 2:
    print("You win!\n")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose!\n")
  elif computer_choice > user_choice:
    print("You lose!!\n")
  elif user_choice > computer_choice:
    print("You win!\n")
  elif computer_choice == user_choice:
    print("DRAW. Play again.\n")

