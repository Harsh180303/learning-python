class User:
    def __init__(self, user_id, username, domain):
        print("\nnew user being created...")
        self.id = user_id
        self.username = username
        self.domain = domain
        self.followers = 0
        # print(self.id)
        # print(self.username)
        # print(self.domain)

user1 = User(18, "Harsh", "Ai/Ml Engineer")

user2 = User(19, "Adarsh", "Junior Dev")

print(user2.followers)