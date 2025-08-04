import random

# Welcome
print("Welcome to the Number Guessing Game!")
answer = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

HARD_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10

should_continue = True

def guess_the_num(turns) :
    while (turns > 0):
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            should_continue = False
        elif guess > answer:
            print("Too high.")
        else:
            print("Too low.")
        turns -= 1

    print(f"You couldn't get the answer, The correct answer was {answer}")


if (difficulty == 'easy'):
    guess_the_num(EASY_LEVEL_TURNS)
else :
    guess_the_num(HARD_LEVEL_TURNS)
