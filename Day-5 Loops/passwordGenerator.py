import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
no_of_letters = int(input("How many letter would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like in your password?\n"))
no_of_digits = int(input("How many digits would you like in your password?\n"))

password = ""

for symb in range(0, no_of_symbols):
    symb = random.choice(symbols)
    password += symb

for dig in range(0, no_of_digits):
    dig = random.choice(numbers)
    password += dig

# left_chars = no_of_letters - (no_of_symbols + no_of_digits)
# for alphabet in range(0, left_chars):
for alphabet in range(0, no_of_letters):
    alphabet = random.choice(letters)
    password += alphabet

# Easy level
print(password)

# Hard level

char_list = []
for char in password:
    char_list.append(char)

print(char_list)
random.shuffle(char_list)
strong_pass = "".join(char_list)
    
print(f"Strong password is: {strong_pass}")