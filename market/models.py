from market import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owner')

    @property
    def pretier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'${str(self.budget)[:-3]},{str(self.budget)[-3:]}'
        else:
            return f'${self.budget}'

    @property
    def password_hash(self):
        return self.password_hash

    @password_hash.setter
    def password_hash(self, plain_text_password):
        self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        if bcrypt.check_password_hash(self.password, attempted_password):
            return True


class Item(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    price = db.Column(db.Integer())
    owner_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'
