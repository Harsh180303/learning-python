from art import logo
# print(logo)
from game_data import data
import random

def getRandomUser() :
    user = random.choice(data)
    return user

user1 = getRandomUser()
user2 = getRandomUser()
print(f"Compare A: {user1["name"]}, a {user1["description"]} from {user1["country"]}")
print(f"Against B: {user2["name"]}, a {user2["description"]} from {user2["country"]}")


choice = input("Who has more followers? Type 'A' or 'B': ").upper()

# print(getRandomUser())