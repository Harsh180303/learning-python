import random

#Step 1 

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

word_list = ["about", "which", "their", "there", "would", "these", "other", "could", "first", "those", "where", "after", "great", "world", "under", "never", "again", "right", "place", "think"]

chosen_word = random.choice(word_list)

print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Please guess a single character\n")
guess_lowercase = guess.lower()
# print(guess_lowercase)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

character_list = []
for char in chosen_word:
    character_list.append(char)

# print(character_list)

for element in character_list:
    if guess == element:
        print("Right")
    else :
        print("Wrong")