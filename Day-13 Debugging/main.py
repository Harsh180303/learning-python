# Problem 1
# range does not include the last digit

"""
def my_function():
    # for i in range(1, 20):
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()
"""

# Problem 2

"""
import random
dice_num = ["1", "2", "3", "4", "5", "6"]
# dice_index = random.randint(1, 6)
dice_index = random.randint(0, 5)
print(dice_num[dice_index])
"""

# Problem 3
"""
# play Computer
year = int(input("What is your year of birth? "))
# if year > 1980 and year < 1994:
if year > 1980 and year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")
"""

# Problem 4
"""
# Fix the Errors
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")
"""

# Problem 5
"""
# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"Pages = {pages}")
print(f"Words per page = {word_per_page}")
print(total_words)
"""

# Problem 6
"""
# Use a Debugger
def mutete(a_list) :
    b_list = []
    for item in a_list:
        new_item = item * 2
    # b_list.append(new_item)  # this should be inside the loop
        b_list.append(new_item)  # like this
    print(b_list)

mutete([1,2,3,5,8,13])
"""

# Problem 7
"""
number = int(input("Which number do you want to check? "))
# if number % 2 = 0: # here we are assigning 0 which is wrong
if number % 2 == 0:
    print("This is an even number.")
else :
    print("This is an odd number.")
"""

# Problem 8
# Leap year Exercise

# year = input("Which year do you want to check? ")  # input is a string here....
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else :
        print("Leap year.")
else :
    print("Not leap year.")