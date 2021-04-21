from flask import Flask, render_template, request, flash, redirect, session
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address!")

    mysql = connectToMySQL('email')
    posted_email = request.form['email']
    email = mysql.query_db(f"SELECT * FROM email.email WHERE email='{posted_email}'")
    print(email)
    if email:
        flash("Duplicated email address!")
    
    if not '_flashes' in session.keys():
        mysql = connectToMySQL('email')
        query = 'INSERT INTO email.email (email, created_at, updated_at)'\
                'VALUES (%(email)s, NOW(), NOW())'
        data = {
            'email': request.form['email'],
        }
        new_post = mysql.query_db(query, data)
        session['email'] = request.form['email']
        return redirect('/success')
    else:
        return redirect('/')

@app.route('/success')
def show_success():
    mysql = connectToMySQL('email')
    emails = mysql.query_db('SELECT * FROM email.email')
    return render_template("success.html", emails=emails)

@app.route('/destroy/<int:id>')
def delete(id):
    mysql = connectToMySQL('email')
    to_delete = mysql.query_db(f'Delete FROM email.email WHERE id={id}')
    session.pop('email', None)
    return redirect('/success')

if __name__=="__main__":
    app.run(debug=True)