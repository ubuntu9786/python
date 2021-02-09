#this is where the different pages are

from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    pass
