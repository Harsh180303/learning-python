import random

word_list = ["about", "which", "their", "there", "would", "these", "other", "could", "first", "those", "where", "after", "great", "world", "under", "never", "again", "right", "place", "think"]

chosen_word = random.choice(word_list)


print(f"(Debug) Chosen word: {chosen_word}")
# I got the chosen word

space_list = []
for space in range(0, len(chosen_word)):
    space_list.append("_")
    # space_list += "_"

# print(space_list)

character_list = []
for char in chosen_word:
    character_list.append(char)

guess_list = []
while "_" in space_list :
    guess = (input("Please guess a single character ")).lower()
    
    for element in character_list:
        if guess == element:
            guess_list.append(guess)
        else :
            guess_list.append("_")

    print(guess_list)