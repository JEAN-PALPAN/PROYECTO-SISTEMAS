from flask import Blueprint, request, render_template
from services.user_service import UserService

main = Blueprint('main', __name__)

class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def index(self):
        users = self.user_service.get_all_users()
        return render_template('index.html', users=users)

    def add_user(self):
        username = request.form['username']
        self.user_service.add_user(username)
        return self.index()

user_service = UserService()
user_controller = UserController(user_service)

@main.route('/')
def index():
    return user_controller.index()

@main.route('/add_user', methods=['POST'])
def add_user():
    return user_controller.add_user()
