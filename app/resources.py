from flask_restx import Resource, Namespace

from .api_models import course_model, student_model
from .models import Course, Student

ns = Namespace("api")


@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"hello": "restx"}
    
@ns.route("/courses")
class CourseAPI(Resource):
    # marshal will coerce course model into json friendly data
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()
    
    @ns.expects(course_model)
    def post(self):
        return {}
    

    
@ns.route("/students")
class StudentAPI(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()