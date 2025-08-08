from art import logo, vs
print(logo)
from game_data import data
import random

def getRandomUser() :
    user = random.choice(data)
    return user

user1 = getRandomUser()
score = 0
win = True
while (win) :
    user2 = getRandomUser()
    while user2 == user1:
        user2 = getRandomUser()
    print(f"Compare A: {user1['name']}, a {user1['description']} from {user1['country']}.")
    print(vs)
    print(f"Against B: {user2['name']}, a {user2['description']} from {user2['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice == 'A' and user1['follower_count'] > user2['follower_count'] :
        score += 1
        print(f"You're right! Current score: {score}")
        user1 = user2

    elif choice == 'B' and user2['follower_count'] > user1['follower_count'] :
        score += 1
        print(f"You're right! Current score: {score}")
        # user1 = user1
    else :
        score = 0
        print(f"Sorry, that's wrong. Final score: {score}")
        win = False
