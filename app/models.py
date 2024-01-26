from .extensions import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)    #every model needs an id
    name = db.Column(db.String(50), unique=True)    #string with 50 char limit


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)  #every model needs an id  
    name = db.Column(db.String(50), unique=True)    #string with 50 char limit
    course_id = db.Column(db.ForeignKey("course.id"))