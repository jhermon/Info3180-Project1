from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'prod'
if ENV == 'dev':
    app.debug =True
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project"
else:
    app.debug =False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pqwpnlmqmcsrws:80ed4b14d3b33ce63d01f76749bfd0d31e4f3be67005cf8e36b7a5219606b462@ec2-54-152-175-141.compute-1.amazonaws.com:5432/dcdj601d2luodu'

app.config['SECRET_KEY'] = "thelordisgod"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.config['UPLOAD_FOLDER'] = "./app/static"
# this is where the images are stored app\static\images

# Flask-Login login manager


app.config.from_object(__name__)
from app import views