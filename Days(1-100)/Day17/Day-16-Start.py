#Creating our own class

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.follower += 1


user1 = User("001", "Piyush")
user2 = User("002", "Varun")
user1.follow(user2)
print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)
