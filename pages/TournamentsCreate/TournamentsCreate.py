from flask import Blueprint, render_template

# TournamentsCreate blueprint definition
TournamentsCreate = Blueprint('TournamentsCreate', __name__, static_folder='static', static_url_path='/TournamentsCreate', template_folder='templates')


# Routes
@TournamentsCreate.route('/TournamentsCreate')
def index():
    return render_template('TournamentsCreate.html')
