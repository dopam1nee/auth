from flask import render_template, request, redirect, url_for
from webapp import app, db
from webapp.models import User

@app.route('/')
def home():
    return 'Home Page'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return 'User registered successfully'
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return 'Logged in successfully'
        else:
            return 'Invalid username or password'
    return render_template('login.html')