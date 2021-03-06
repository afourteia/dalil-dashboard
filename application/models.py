from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin
from application import db, login_manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


# class HealthFacility(db.Model):
#     __tablename__ = 'health_facilites'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True, nullable=False)
#     facility_type = db.Column(db.String(20), nullable=False)
#     location = db.Column(db.String(120))
#     email = db.Column(db.String(120))


# class membership(db.Model):
#     __tablename__ = 'members'
#     id = db.Column(db.Integer, primary_key=True)
#     member_name = db.Column(db.String(120), nullable=False)
#     benefciary_name = db.Column(db.String(20), nullable=False)
#     location = db.Column(db.String(120))
#     email = db.Column(db.String(120))


# class expense(db.Model):
#     __tablename__ = 'health_facilites'
#     internal_id = db.Column(db.Integer, primary_key=True)
#     member = db.Column(db.String(64), unique=True, nullable=False)
#     facility_type = db.Column(db.String(20), nullable=False)
#     location = db.Column(db.String(120))
#     email = db.Column(db.String(120))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
