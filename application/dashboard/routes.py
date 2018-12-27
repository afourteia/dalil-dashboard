from flask import Blueprint, render_template, url_for

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/dashboard')
def plot():
    return render_template('dashboard.html', title='dashboard')
