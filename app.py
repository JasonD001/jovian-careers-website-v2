# from flask import Flask, render_template, jsonify, abort, request
# from database import engine , add_application_to_db
# from sqlalchemy import text


# def load_jobs_from_db():
#     with engine.connect() as conn:
#         print("Connected to the database.")
#         result = conn.execute(text("SELECT * FROM jobs"))
#         jobs = []
#         for row in result.mappings():  # Using mappings() to get dictionary-like row
#             jobs.append(dict(row))
#         print("Jobs loaded:", jobs)
#         return jobs

# def load_job_from_db(job_id):
#     with engine.connect() as conn:
#         print(f"Fetching job with ID: {job_id}")
#         result = conn.execute(text("SELECT * FROM jobs WHERE id = :job_id"), {"job_id": job_id})
#         job = result.mappings().first()
#         if job:
#             print("Job found:", job)
#             return dict(job)
#         else:
#             print("Job not found")
#             return None

# app = Flask(__name__)

# @app.route("/")
# def hello_jovian():
#     jobs = load_jobs_from_db()
#     return render_template('home.html', jobs=jobs, company_name='Jovian')

# @app.route("/api/jobs")
# def list_jobs():
#     jobs = load_jobs_from_db()  # Load jobs from the database
#     return jsonify(jobs)

# @app.route("/job/<int:job_id>")
# def get_job(job_id):
#     try:
#         job = load_job_from_db(job_id)
#         if job:
#             print("Rendering job:", job)
#             return render_template('jobpage.html', job=job)
#         else:
#             abort(404, description="Job not found")
#     except Exception as e:
#         print(f"Error occurred: {e}")
#         abort(500, description="Internal Server Error")



# @app.route("/job/<id>/apply", methods=['POST'])
# def apply_to_job(id):
#     data = request.form

#     # getting information about the job here for the database
#     job = load_job_from_db(id)

#     # its going to populate the job id coloumn
#     add_application_to_db(id, data) 
    
#     # You can add more logic to handle the application data here
#     return render_template('application_submitted.html', application= data, job=job)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5001, debug=True)

#--------------------------------------------------------------------

from flask import Flask, render_template, jsonify, abort, request
from database import engine, add_application_to_db
from sqlalchemy import text

def load_jobs_from_db():
    with engine.connect() as conn:
        print("Connected to the database.")
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.mappings():  # Using mappings() to get dictionary-like row
            jobs.append(dict(row))
        print("Jobs loaded:", jobs)
        return jobs

def load_job_from_db(job_id):
    with engine.connect() as conn:
        print(f"Fetching job with ID: {job_id}")
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :job_id"), {"job_id": job_id})
        job = result.mappings().first()
        if job:
            print("Job found:", job)
            return dict(job)
        else:
            print("Job not found")
            return None

app = Flask(__name__)

@app.route("/")
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()  # Load jobs from the database
    return jsonify(jobs)

@app.route("/job/<int:job_id>")
def get_job(job_id):
    try:
        job = load_job_from_db(job_id)
        if job:
            print("Rendering job:", job)
            return render_template('jobpage.html', job=job)
        else:
            abort(404, description="Job not found")
    except Exception as e:
        print(f"Error occurred: {e}")
        abort(500, description="Internal Server Error")

@app.route("/job/<id>/apply", methods=['POST'])
def apply_to_job(id):
    data = request.form

    # getting information about the job here for the database
    job = load_job_from_db(id)

    # its going to populate the job id coloumn
    add_application_to_db(id, data) 

    # You can add more logic to handle the application data here
    return render_template('application_submitted.html', application= data, job=job)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
