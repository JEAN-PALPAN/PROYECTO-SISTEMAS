from models import UserModel

class UserService:
    def __init__(self):
        self.user_model = UserModel()

    def get_all_users(self):
        return self.user_model.get_all_users()

    def add_user(self, username):
        self.user_model.add_user(username)
