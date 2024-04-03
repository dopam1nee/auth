from flask import Blueprint, render_template, request, url_for
from .models import User
#from webapp.user_sessions import user_sessions, create_session, remove_session
bp = Blueprint('main', __name__)

active_users = []

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    global reg_username
    if request.method == 'POST':
        reg_username = request.form['username']
        reg_password = request.form['password']
        is_online = True

        user = User(reg_username, reg_password, is_online)
        
        #global hash
        #hash = create_session(user)
        #print('USER_SESSIONS:', user_sessions)

        active_users.append(user)

        return render_template('registered.html')
    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        log_username = request.form['username']
        reg_password = request.form['password']
        
        for user in active_users:
            if user.username == log_username and user.password == reg_password:
                user.is_online = True
                
                return render_template('logged.html')
        return "Invalid username or password"
    return render_template('login.html')

@bp.route('/offline', methods=['GET', 'POST'])
def offline():
    for user in active_users:
      if user.username == reg_username:
        user.is_online = False
        #remove_session(hash)
        #print('AFTER DEL:', user_sessions)

@bp.route('/users')
def users():
    return render_template('users.html', active_users=active_users)
