from flask_cors import CORS
from flask import Flask, jsonify, request, Response

from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema

import json
import time
import atexit
import threading

# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)

@app.route('/time')
def get_time():
    return Response(json.dumps({'time': str(time.time()) }))

@app.route('/exams')
def get_exams():
    # fetching from the database
    session = Session()
    exam_objects = session.query(Exam).all()

    # transforming into JSON-serializable objects
    schema = ExamSchema(many=True)
    exams = schema.dump(exam_objects)

    # serializing as JSON
    session.close()
    return Response(json.dumps(exams))

@app.route('/exams', methods=['POST'])
def add_exam():
    # mount exam object
    posted_exam = ExamSchema(only=('title', 'description'))\
        .load(request.get_json())

    exam = Exam(**posted_exam.data, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(exam)
    session.commit()

    # return created exam
    new_exam = ExamSchema().dump(exam).data
    session.close()
    return jsonify(new_exam), 201

##################################
## BACKGROUND PROCESS CODE      ##
##################################

def background_job():
    global backgroundThread
    global dataLock

    with dataLock:
        print('This job is run every 30 seconds.')
    
    # set the next thread to happen
    backgroundThread = threading.Timer(30, background_job, ())
    backgroundThread.start()

# create a datalock
dataLock = threading.Lock()

# create a background scheduler running on background thread
backgroundThread = threading.Thread()
backgroundThread = threading.Timer(30, background_job, ())
backgroundThread.start()

##################################
## END BACKGROUND PROCESS CODE  ##
##################################

if __name__ == "__main__":
    app.run()