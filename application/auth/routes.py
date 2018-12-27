from flask import Blueprint, render_template, request, url_for, flash, redirect
from flask_login import login_user, logout_user, login_required
from .forms import RegistrationForm, LoginForm
from ..models import User
from application import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        # Query the database and filter by the provided email
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash('Log in successful!', 'success')
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        else:
            flash('Login unsucessful, please check username and password', 'danger')
    return render_template('login.html', form=form, title='login')


@auth.route("/register", methods=['GET', 'POST'])
def register():
    flash('This feature is not activated!', 'warning')
    flash('هذه الخـدمــة غيــر مفعلة حاليا', 'warning')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('errors.construction'))
    return render_template('register.html', title='Register', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'warning')
    return redirect(url_for('main.index'))
