import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'quiz.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import models
import routes

if __name__ == '__main__':
    print("Starting Flask on http://127.0.0.1:5000 …")
    app.run(debug=True)