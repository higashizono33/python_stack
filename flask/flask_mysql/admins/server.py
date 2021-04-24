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
        
        if request.form['confirm_pw'] != request.form['password']:
            flash("Confirm Password doesn't match with the above", "confirm_pw")
        if not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid email address!", "email")
        
        mysql = connectToMySQL('admins')
        posted_email = request.form['email']
        email = mysql.query_db(f"SELECT * FROM admins.user WHERE email='{posted_email}'")
        if email:
            flash("The email address is already token", "email")
        
        if not '_flashes' in session.keys():
            pw_hash = bcrypt.generate_password_hash(request.form['password']) 
            mysql = connectToMySQL('admins')
            query = 'INSERT INTO admins.user (first_name, last_name, email, password, user_level, created_at, updated_at)'\
                    'VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s, %(user_level)s, NOW(), NOW())'
            data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'password_hash': pw_hash,
                'user_level': 1,
            }
            new_user = mysql.query_db(query, data)

            mysql = connectToMySQL('admins')
            query = "SELECT * FROM admins.user WHERE email = %(email)s;"
            data = { "email" : request.form["email"] }
            result = mysql.query_db(query, data)
            session['userid'] = result[0]['id']
            session['userlevel'] = result[0]['user_level']
            if result[0]['user_level'] == 9:
                return redirect('/admin')
            else:
                return redirect('/user')
        else:
            return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL('admins')
    query = "SELECT * FROM admins.user WHERE email = %(email)s;"
    data = { "email" : request.form["email"] }
    result = mysql.query_db(query, data)
    if len(result) > 0:
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            session['userid'] = result[0]['id']
            session['userlevel'] = result[0]['user_level']
            if result[0]['user_level'] == 9:
                return redirect('/admin')
            else:
                return redirect('/user')
    flash("You could not be logged in", "login")
    return redirect("/")

@app.route('/admin')
def show_admin_home():
    if session.get('userlevel') != 9:
        return redirect('/danger')
    mysql = connectToMySQL('admins')
    users = mysql.query_db('SELECT * FROM admins.user;')
    mysql = connectToMySQL('admins')
    query = 'SELECT * FROM admins.user WHERE id = %(userid)s;'
    data = { "userid" : session["userid"] }
    logged_user = mysql.query_db(query, data)
    return render_template("admin_home.html", users=users, logged_user=logged_user)

@app.route('/user')
def show_user_home():
    if 'userid' not in session:
        return redirect('/')
    mysql = connectToMySQL('admins')
    query = 'SELECT * FROM admins.user WHERE id = %(userid)s;'
    data = { "userid" : session["userid"] }
    user = mysql.query_db(query, data)
    return render_template("user_home.html", user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/danger', methods=['GET'])
def warning():
    session.clear()
    ip_address = request.remote_addr
    return render_template("warning.html", ip_address=ip_address)

@app.route('/remove/<int:id>')
def remove_user(id):
    if session.get('userlevel') != 9:
        return redirect('/danger')
    mysql = connectToMySQL('admins')
    query = "DELETE FROM admins.user WHERE id = %(user_id)s;"
    data = { "user_id" : id }
    result = mysql.query_db(query, data)
    return redirect("/admin")

@app.route('/remove_admin/<int:id>')
def remove_admin(id):
    if session.get('userlevel') != 9:
        return redirect('/danger')
    mysql = connectToMySQL('admins')
    query = "UPDATE admins.user SET user_level=1 WHERE id = %(user_id)s;"
    data = { "user_id" : id }
    result = mysql.query_db(query, data)
    return redirect("/admin")

@app.route('/make_admin/<int:id>')
def make_admin(id):
    if session.get('userlevel') != 9:
        return redirect('/danger')
    mysql = connectToMySQL('admins')
    query = "UPDATE admins.user SET user_level=9 WHERE id = %(user_id)s;"
    data = { "user_id" : id }
    result = mysql.query_db(query, data)
    return redirect("/admin")

if __name__=="__main__":
    app.run(debug=True)
