from . import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_online = db.Column(db.Boolean, default=False)

    def __init__(self, username, password, is_online):
        self.username = username
        self.password = password
        self.is_online = is_online
