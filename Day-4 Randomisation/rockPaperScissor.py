import random

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
computer_choice = random.randint(0, 2)

# MY CHOICE
if my_choice == 0:
    choice_by_me = "Rock"
elif my_choice == 1:
    choice_by_me = "Paper"
else:
    choice_by_me = "Scissors"

# COMPUTER CHOICE
if computer_choice == 0:
    choice_by_computer = "Rock"
elif computer_choice == 1:
    choice_by_computer = "Paper"
else:
    choice_by_computer = "Scissors"

print(f"You choose: {choice_by_me}")

print(f"Computer choose: {choice_by_computer}")

# Case 1
if my_choice == 0 and computer_choice == 2:
    print("You Win!")
elif my_choice == 1 and computer_choice == 0:
    print("You Win!")
elif my_choice == 2 and computer_choice == 1:
    print("You Win!")
elif my_choice == computer_choice:
    print("Match draw")
else:
    print("You Lose")