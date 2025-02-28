import random

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

import random
list1 = [rock, paper, scissors]

user = input('choose "paper, rock, or scissors" ').lower()
if user == "paper":
    print(list1[1])
if user == "rock":
    print(list1[0])
if user == "scissors":
    print(list1[2])

print("Computer choose: ")
computer_choice = random.choice(list1)
print(computer_choice)

if user == "paper" and computer_choice == paper:
    print("Draw")
if user == "paper" and computer_choice == rock:
    print("You win!")
if user == "paper" and computer_choice == scissors:
    print("You lose")

if user == "scissors" and computer_choice == paper:
    print("You win!")
if user == "scissors" and computer_choice == rock:
    print("You lose!")
if user == "scissors" and computer_choice == scissors:
    print("Draw")

if user == "rock" and computer_choice == paper:
    print("You lose")
if user == "rock" and computer_choice == rock:
    print("Draw")
if user == "rock" and computer_choice == scissors:
    print("You win!")

input("press any key to exit")
