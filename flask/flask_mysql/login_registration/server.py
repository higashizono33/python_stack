from flask import Flask, render_template, request, flash, redirect, session
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt
from datetime import date, datetime

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
bcrypt = Bcrypt(app) 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        if len(request.form['first_name']) < 1:
            flash("Please enter your first name", "first_name")
        if len(request.form['last_name']) < 1:
            flash("Please enter your last name", "last_name")
        if len(request.form['password']) < 8:
            flash("Password should be at least 8 characters", "password")
        else:
            num_check = False
            upper_check = False
            for i in request.form['password']:
                if i.isnumeric():
                    num_check = True
                if i.isupper():
                    upper_check = True
            if not num_check or not upper_check:
                flash("Password should contain at least 1 number and uppercase", "password")
        
        if request.form['confirm_pw'] != request.form['password']:
            flash("Confirm Password doesn't match with the above", "confirm_pw")
        if not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid email address!", "email")
        if len(request.form['birthday']) < 1:
            flash("Please enter your birthday", "birthday")
        else:
            birthday = datetime.strptime(request.form['birthday'], "%Y-%m-%d")
            today = date.today()
            age = (today - date(birthday.year, birthday.month, birthday.day)).days / 365
            if age < 18:
                flash("You must be order than 18 years old", "birthday")

        mysql = connectToMySQL('login_registration')
        posted_email = request.form['email']
        email = mysql.query_db(f"SELECT * FROM login_registration.user WHERE email='{posted_email}'")
        if email:
            flash("The email address is already token", "email")
        
        if not '_flashes' in session.keys():
            pw_hash = bcrypt.generate_password_hash(request.form['password']) 
            mysql = connectToMySQL('login_registration')
            query = 'INSERT INTO login_registration.user (first_name, last_name, email, password, birthday, created_at, updated_at)'\
                    'VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s, %(birthday)s, NOW(), NOW())'
            data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'password_hash': pw_hash,
                'birthday': request.form['birthday'],
            }
            new_user = mysql.query_db(query, data)

            mysql = connectToMySQL('login_registration')
            query = "SELECT * FROM login_registration.user WHERE email = %(email)s;"
            data = { "email" : request.form["email"] }
            result = mysql.query_db(query, data)
            session['userid'] = result[0]['user_id']
            return redirect('/success')
        else:
            return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL('login_registration')
    query = "SELECT * FROM login_registration.user WHERE email = %(email)s;"
    data = { "email" : request.form["email"] }
    result = mysql.query_db(query, data)
    if len(result) > 0:
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            session['userid'] = result[0]['user_id']
            return redirect('/success')
    flash("You could not be logged in", "login")
    return redirect("/")

@app.route('/success')
def show_success():
    if 'userid' not in session:
        return redirect('/')
    mysql = connectToMySQL('login_registration')
    query = 'SELECT * FROM login_registration.user WHERE user_id = %(userid)s;'
    data = { "userid" : session["userid"] }
    user = mysql.query_db(query, data)
    print(user)
    return render_template("success.html", user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)