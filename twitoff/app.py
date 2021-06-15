""" 
Main app/ routing file for Twitoff application.
File we call in the init file to initialize.
"""

from flask import Flask, render_template
from .models import DB, User, Tweet


def create_app():
    # Initialize the application
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    

    @app.route("/")
    def root():
        """My base home url """
        DB.drop_all()
        DB.create_all()
        insert_example_users()
        users = User.query.all()
        return render_template("base.html", title='Home', users=users)
        
    DB.init_app(app)

    @app.route ('/some_branch')
    def some_branch():
        """What I will do in this branch"""
        print('I am a secondary branch')

    return app

def insert_example_users():
    """
    Will get error if ran twice because of duplicate primary keys
    Not real data - just to play with
    """
    nvidia = User(id=1, name="Nvidia")
    dasani = User(id=2, name="DasaniWater")
    valyouf = User(id=3, name="Valyou Furniture")
    DB.session.add(nvidia)
    DB.session.add(User(id=2, name="DasaniWater"))
    DB.session.add(User(id=3, name="Valyou Furniture"))
    DB.session.commit()

    # valyouf Sometimes, Art Design can help inspire a room collection.  Soft colors and gold accents is a great modern vibe.

# def insert_tweets():
#     nvidia_t1 = Tweet(id=1, text="Ready for art and design", user_id=1, user=,)