from project import db
import datetime
#from project import engine, Base
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import ForeignKey,Column, Integer,String, Date
#from sqlalchemy.orm import relationship



class Courses(db.Model):

    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)


    def __init__(self,name=None,duration=None):
        self.name = name
        self.duration = duration

class Instructors(db.Model):

    __tablename__ = "instructors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable=False)

    def __init__(self,name=None):
        self.name = name

class Classes(db.Model):

    __tablename__ = "classes"

    id = db.Column(db.Integer, primary_key=True)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructors.id'))
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)


    def __init__(self,instructor=None,start_date=None,end_date=None):
        self.instructor = instructor
        self.start_date = start_date
        self.end_date = end_date

class Users(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), unique=True, nullable=False)
    email = db.Column(db.String(length=50), unique=True, nullable=False)
    password = db.Column(db.String(length=50), nullable=False)
    courses = db.relationship('Classes')
    role = db.Column(db.String(length=50), default='user')

    def __init__(self, name=None, email=None,password=None,role=None):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
