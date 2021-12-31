from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

<<<<<<< HEAD
## SignIn
from pages.SignIn.SignIn import SignIn
app.register_blueprint(SignIn)

## About
from pages.about.about import about
app.register_blueprint(about)
=======
>>>>>>> e393733a75eb83cb8704f89e7ab9b37906e11691

## Catalog
from pages.TournamentsCreate.TournamentsCreate import TournamentsCreate
app.register_blueprint(TournamentsCreate)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)
