# from flask import Flask, render_template, jsonify, abort
# from database import engine
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

# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template('404.html', error=error), 404

# @app.errorhandler(500)
# def internal_error(error):
#     return render_template('500.html', error=error), 500

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', debug=True)


# -----------------------

# import os
# from flask import Flask, render_template, jsonify, request, abort
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import text

# app = Flask(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')

# # Initialize SQLAlchemy
# db = SQLAlchemy(app)

# # Define the Application model
# class Application(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     job_id = db.Column(db.Integer)
#     fullname = db.Column(db.String(100))
#     email = db.Column(db.String(100))
#     linkedin = db.Column(db.String(100))
#     experience = db.Column(db.Text)

# def load_jobs_from_db():
#     try:
#         with app.app_context():
#             print("Connected to the database.")
#             result = db.engine.execute("SELECT * FROM jobs")
#             jobs = [dict(row) for row in result]
#             print("Jobs loaded:", jobs)
#             return jobs
#     except Exception as e:
#         print(f"Error loading jobs from database: {e}")
#         return []

# def load_job_from_db(job_id):
#     try:
#         with app.app_context():
#             print(f"Fetching job with ID: {job_id}")
#             result = db.engine.execute("SELECT * FROM jobs WHERE id = :job_id", {"job_id": job_id})
#             job = dict(result.first())
#             if job:
#                 print("Job found:", job)
#                 return job
#             else:
#                 print("Job not found")
#                 return None
#     except Exception as e:
#         print(f"Error loading job from database: {e}")
#         return None

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

# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template('404.html', error=error), 404

# @app.errorhandler(500)
# def internal_error(error):
#     return render_template('500.html', error=error), 500

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', debug=True)


from flask import Flask, render_template, jsonify, abort, request
from database import engine
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

# Route to display the application form
@app.route('/job/<int:job_id>/apply', methods=['GET'])
def show_application_form(job_id):
    return render_template('application_form.html', job={'id': job_id})

# Route to handle form submission
@app.route('/job/<int:job_id>/apply', methods=['POST'])
def apply_for_job(job_id):
    fullname = request.form['fullname']
    email = request.form['email']
    linkedin = request.form['linkedin']
    experience = request.form['experience']
    education = request.form['education']
    work_experience = request.form['work_experience']

    # Insert form data into the database
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO applications (job_id, fullname, email, linkedin, experience, education, work_experience) "
                 "VALUES (:job_id, :fullname, :email, :linkedin, :experience, :education, :work_experience)"),
            {
                'job_id': job_id,
                'fullname': fullname,
                'email': email,
                'linkedin': linkedin,
                'experience': experience,
                'education': education,
                'work_experience': work_experience
            }
        )

    return "Application submitted successfully!"


@app.route("/applications")
def list_applications():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM applications"))
        applications = [dict(row) for row in result.mappings()]
        return render_template('applications.html', applications=applications)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', error=error), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5001, debug=True)
