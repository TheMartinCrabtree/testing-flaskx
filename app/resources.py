from flask_restx import Resource, Namespace

from .api_models import course_model
from .models import Course

ns = Namespace("api")


@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"hello": "restx"}
    
@ns.route("/courses")
class CourseAPI(Resource):
    # coerce course model into json friendly data
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()