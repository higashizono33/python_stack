from flask import Flask, render_template, request, flash, redirect, session
from mysqlconnection import connectToMySQL
from datetime import date, datetime

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/dashboard')
def index():
    mysql = connectToMySQL('report_card')
    students = mysql.query_db('SELECT * FROM report_card.student')
    return render_template("index.html", students=students)

@app.route('/<int:student_id>')
def grade_show(student_id):
    session['student_id'] = student_id
    mysql = connectToMySQL('report_card')
    query = 'SELECT * FROM report_card.grade JOIN report_card.student ON report_card.grade.student_id = report_card.student.id '\
    'JOIN report_card.course ON report_card.grade.course_id = report_card.course.id WHERE student_id = %(student_id)s;'
    data = {
        'student_id': student_id,
    }
    grades = mysql.query_db(query, data)
    mysql = connectToMySQL('report_card')
    student = mysql.query_db(f'SELECT * FROM report_card.student WHERE id={student_id}')
    return render_template("card.html", grades=grades, student=student)

@app.route('/edit/<int:student_id>')
def edit(student_id):
    session['student_id'] = student_id
    mysql = connectToMySQL('report_card')
    courses = mysql.query_db('SELECT * FROM report_card.course')
    return render_template("edit.html", courses=courses)

@app.route('/edit/<int:student_id>/add_grade', methods=["POST"])
def add_grade(student_id):
    if request.method == 'POST':
        if len(request.form['course_name']) < 1:
            flash("Please enter course name")
        if len(request.form['grade']) < 1:
            flash("Please select the grade")
        if len(request.form['date']) < 1:
            flash("Please enter the date")
        
        if not '_flashes' in session.keys():
            mysql = connectToMySQL('report_card')
            query = 'INSERT INTO report_card.grade (student_id, course_id, grade, comment, created_at, updated_at)'\
                    'VALUES (%(student_id)s, %(course_id)s, %(grade)s, %(comment)s, %(date)s, NOW())'
            data = {
                'student_id': student_id,
                'course_id': int(request.form['course_name']),
                'grade': request.form['grade'],
                'comment': request.form['comment'],
                'date': request.form['date'],
            }
            add_grade = mysql.query_db(query, data)
            return redirect('/dashboard')
        else:
            return redirect(f'/edit/{student_id}')

if __name__=="__main__":
    app.run(debug=True)