from flask import Blueprint, render_template

# SignIn blueprint definition
SignIn = Blueprint('SignIn', __name__, static_folder='static', static_url_path='/SignIn', template_folder='templates')


# Routes
@SignIn.route('/SignIn')
def index():
    return render_template('SignIn.html')
