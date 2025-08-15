class User:
    def __init__(self, user_id, username, domain):
        print("\nnew user being created...")
        self.id = user_id
        self.username = username
        self.domain = domain
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User(18, "Harsh", "Ai/Ml Engineer")

user2 = User(19, "Adarsh", "Junior Dev")

user2.follow(user1)
print(f" {user1.username}'s followers are: {user1.followers}")
print(f" {user1.username}'s following are: {user1.following}")
print(f" {user2.username}'s followers are: {user2.followers}")
print(f" {user2.username}'s following are: {user2.following}")