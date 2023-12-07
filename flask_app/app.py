from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'

db = SQLAlchemy(app)
app.app_context().push()

from routes import *

if __name__ == '__main__':
    app.run(debug=True)