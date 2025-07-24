import random

from hangmanWords import word_list
from hangmanArt import stages

chosen_word = random.choice(word_list)
lives = 6

from hangmanArt import logo
print(logo)

print(f"(Debug) Chosen word: {chosen_word}")

display = []
for _ in chosen_word:
    display += "_"

print(display)

end_of_game = False

while not end_of_game :
    guess = (input("Please guess a single character ")).lower()
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. You lost a life. Lives left: {lives}")
        if lives >= 0:
            print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose")

    if not end_of_game:
        print(display)

    if not "_" in display:
        end_of_game = True
        print("You Win!")
