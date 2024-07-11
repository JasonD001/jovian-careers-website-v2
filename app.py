# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#   return render_template('home.html')

# print(__name__)
# if __name__ == "__main__":
#   app.run(host='0.0.0.0', debug=True)

#jsonify - converst into to json things Convert Data to JSON:
#------------------------------
# from flask import Flask, render_template, jsonify


# app = Flask(__name__)

# JOBS = [{
#     "id": 1,
#     "title": "Data Analyst",
#     "location": "Bengaluru, India",
#     "salary": "Rs. 10,00,000"
# }, {
#     "id": 2,
#     "title": "Data Scientist",
#     "location": "Delhi, India",
#     "salary": "Rs. 15,00,000"
# }, {
#     "id": 3,
#     "title": "Data Engineer",
#     "location": "Hyderabad, India",
#     "salary": "Rs. 12,00,000"
# }, {
#     "id": 4,
#     "title": "DevOps",
#     "location": "Noida, India",
#     "salary": "$50,000"
# }]


# @app.route("/")
# def hello_world():
#   return render_template('home.html', jobs=JOBS, company_name='Jovian')

# # ("/api") - means it does not return any html it returns some strutured jason data

# @app.route("/api/jobs")
# def list_jobs():
#   return jsonify(JOBS)


# if __name__ == "__main__":
#   app.run(host='0.0.0.0', debug=True)


#-----------------------------
from flask import Flask, render_template, jsonify
from database import engine 
from sqlalchemy import text 

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.mappings():  # Using mappings() to get dictionary-like row
            jobs.append(dict(row))
        return jobs

app = Flask(__name__)

@app.route("/")
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()  # Load jobs from the database
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
