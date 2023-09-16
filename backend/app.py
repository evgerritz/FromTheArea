import enum
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_restful import reqparse, Api, Resource
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Enum
from sqlalchemy.orm import declarative_base, relationship

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somerandomstring69'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fromthearea.db'

db = SQLAlchemy(app)
Base = declarative_base()

# create the API
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')
class Message(Resource):
    def get(self):
        return {"message": 'Hello World'}
api.add_resource(Message, '/api/hello')

@app.route('/')
def home():
    return 'Home Page Route'

class TypeEnum(enum.Enum):
    restaurant = 1
    bar = 2

'''
DO NOT RUN UNCOMMENT AND RUN THIS CODE
OR IT WILL BE A PAIN TO CHANGE. THESE ARE
SHORT EXAMPLES OF A SQLALCHEMY DB THAT WE 
WILL USE. NEED TO FIGURE OUT DATABASE SCHEMA
class User(Base, db.Model, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

class Venue(Base, db.Model):
    __tablename__ = "venue"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rating = Column(Float)

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    typ = db.Column(db.Enum(TypeEnum))
    address = db.Columm(db.String(100), nummable=False)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()
'''

if __name__ == '__main__':
    app.run(debug=True)

