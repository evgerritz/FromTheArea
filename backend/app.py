from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somerandomstring69'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fromthearea.db'


db = SQLAlchemy(app)
Base = declarative_base()

'''DO NOT RUN UNCOMMENT AND RUN THIS CODE
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

with app.app_context():
    db.create_all()
'''




