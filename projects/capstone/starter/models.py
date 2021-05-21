import os
import json
from sqlalchemy import Column, DateTime, Integer, String, VARCHAR, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#database_name = 'capstonedb'
#database_path = 'postgres://{}/{}'.format('localhost:5432', database_name)
database_path = os.environ['DATABASE_URL']
#database_path = 'postgres://postgres:postgres@localhost:5432/postgres'

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    db.app = app
    db.init_app(app)
    db.create_all()

class Movie(db.Model):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


class Actor(db.Model):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

#class Role(db.Model):
#    __tablename__ = 'Role'
#
#    id = Column(Integer, primary_key=True)
#    type = Column(String)
#
#    def __init__(self, type):
#        self.type = type
#
#    def format(self):
#        return{
#            'id': self.id,
#            'type': self.type
#        }
