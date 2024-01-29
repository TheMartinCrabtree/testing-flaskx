# reference: https://www.youtube.com/watch?v=Qf0wri9MvMY

# create environment
    python -m venv env

# activate vinv env in powershell:
    Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
    ./env/Scripts/activate.ps1

# install flask, flask-restx (api library), flask-sqlalchemy, python-dotenv
    pip install flask
    pip install flask-restx
    pip install flask-sqlalchemy
    pip install python-dotenv

# setup debug mode with .flaskenv file with "FLASK_DEBUG=True"

# setup app and initialize flask

    to run: flask run

# set and update db 
    flask shell
    from app.models import *
    db.create_all()
    exit()

# verify that Students in the db is getting populated
    sqlite3 instance/db.sqlite3
    select * from student;