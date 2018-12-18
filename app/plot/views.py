from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from . import plot


@plot.route('/visualize')
@login_required
def visualize():
    flash('you are entering the dashboard.')
    # return render_template((url_for('plot.visualize')))
    return render_template('plot/visualize.html')
