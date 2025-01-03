class User:
    def __init__(self,name):
        self.name = name
        # self.age = age
        # self.email = email
        self.following = 0
        self.followers = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1

# user = User()
#
#
# user.name = "kashish"
# user.age = 20
# user.email = "kashish@gmail.com"


# user2 = User("kashish",20,"kashishupadhyay145@gmail.com")
#
#
# print(user2.name)
# print(user2.age)
# print(user2.email)

user1 = User("kashish")
user2 = User("roff")

user1.follow(user2)

print(f"user1 following = {user1.following}")
print(f"user1 following = {user1.followers}")