from flask import Blueprint, render_template, url_for, flash, redirect
# from flask_login import login_user, logout_user, login_required
from .forms import RegistrationForm, LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'test' and form.password.data == 'test1':
            flash('You have been logged in!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Login unsucessful, please check username and password', 'danger')
    return render_template('login.html', form=form, title='login')


@auth.route("/register", methods=['GET', 'POST'])
def register():
    flash('This feature is not activated!', 'warning')
    flash('هذه الخـدمــة غيــر مفعلة حاليا', 'warning')
    form = RegistrationForm()
    if form.validate_on_submit():
        # flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('errors.construction'))
    return render_template('register.html', title='Register', form=form)
