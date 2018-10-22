from flask import Blueprint, render_template, url_for

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/')
def home():
    return render_template('page/home.html')
