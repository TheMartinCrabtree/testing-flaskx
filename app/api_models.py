from flask_restx import fields

from .extensions import api

course_model = api.model("Course", {
    "id": fields.Integer,
    "name": fields.String
    #"students":
})