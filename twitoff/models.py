""" SQLAlchemy models for twitoff"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    # Creating the user table
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String, nullable=False)

    def __repr__(self):	
        return f"<User: {self.name}>"

class Tweet(DB.Model):
    # Creating the tweet table
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'))
    user = DB.relationship("User", backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return f"<User: {self.text}>"

# if __name__ == "__main__":
#     DB.create_all()    # SQL Alchemy initiation for initial configuration
#     app.run(debug=True)
