# class User:
#     pass

# user_1 = User()
# user_1.id = "007"
# user_1.username = "agent"

# print(user_1.username)

# user_2 = User()
# user_2.id = "007"
# user_2.username = "agent too"

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 #default value of the attribute "followers"
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("007", "agent")
user_2 = User("007", "agent too")

user_2.follow(user_1)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
