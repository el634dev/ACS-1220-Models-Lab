"""Import packages and modules."""
import os
from flask import Blueprint, request, render_template, redirect, url_for, flash, request
from datetime import date, datetime
from books_app.models import User, Book, Author, Genre

# Import app and db from events_app package so that we can run app
from books_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    """Home Page"""
    # Make a query for all instances of 'User' and send to the template
    users = User.query.all()
    return render_template('home.html', users=users)

@main.route('/profile/<username>')
def profile(username):
    """Profile"""
    # Make a query for the user with the given username, and send to the
    # template
    user_name = request.args.get('username')
    username = User.query.filter_by(username=user_name)
    return render_template('profile.html', username=username)
