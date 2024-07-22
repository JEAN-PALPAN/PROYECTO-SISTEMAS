class UserModel:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_all_users(self):
        return self.users
