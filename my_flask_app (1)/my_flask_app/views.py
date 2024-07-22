from flask import render_template

def show_users(users):
    return render_template('index.html', users=users)
