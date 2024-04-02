from flask import Blueprint, render_template, request, url_for
from .models import User
bp = Blueprint('main', __name__)

active_users = []

@bp.route('/')
def home():
    return 'Home Page'

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User(username, password)
        active_users.append(user)

        return f"Registered user: {username}"
    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in active_users:
            if user.username == username and user.password == password:
                return f"Logged in as: {username}"
        
        return "Invalid username or password"
    return render_template('login.html')

@bp.route('/logout', methods=['POST'])
def logout():
    if request.method == 'POST':
        username = request.form['username']

        for user in active_users:
            if user.username == username:
                active_users.remove(user)
                break

        return "Logged out successfully"

@bp.route('/users')
def users():
    current_user = None
    if active_users:
        current_user = active_users[-1]

    return render_template('users.html', active_users=active_users, current_user=current_user)
