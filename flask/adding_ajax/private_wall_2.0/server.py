from flask import Flask, render_template, request, flash, redirect, session, jsonify, Response
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

        mysql = connectToMySQL('private_wall')
        posted_username = request.form['username']
        username = mysql.query_db(f"SELECT * FROM private_wall.user WHERE username='{posted_username}'")
        if username:
            flash("Username is already token", "username")
        mysql = connectToMySQL('private_wall')
        posted_email = request.form['email']
        email = mysql.query_db(f"SELECT * FROM private_wall.user WHERE email='{posted_email}'")
        if email:
            flash("The email address is already token", "email")
        
        if not '_flashes' in session.keys():
            pw_hash = bcrypt.generate_password_hash(request.form['password']) 
            mysql = connectToMySQL('private_wall')
            query = 'INSERT INTO private_wall.user (username, first_name, last_name, email, password, created_at, updated_at)'\
                    'VALUES (%(username)s, %(first_name)s, %(last_name)s, %(email)s, %(password_hash)s, NOW(), NOW())'
            data = {
                'username': request.form['username'],
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'password_hash': pw_hash,
            }
            new_user = mysql.query_db(query, data)

            mysql = connectToMySQL('private_wall')
            query = "SELECT * FROM private_wall.user WHERE email = %(email)s;"
            data = { "email" : request.form["email"] }
            result = mysql.query_db(query, data)
            session['userid'] = result[0]['id']
            return redirect('/wall')
        else:
            return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL('private_wall')
    query = "SELECT * FROM private_wall.user WHERE email = %(email)s;"
    data = { "email" : request.form["email"] }
    result = mysql.query_db(query, data)
    if len(result) > 0:
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            session['userid'] = result[0]['id']
            return redirect('/wall')
    flash("You could not be logged in", "login")
    return redirect("/")

@app.route('/wall')
def show_wall():
    if 'userid' not in session:
        return redirect('/')
    mysql = connectToMySQL('private_wall')
    query = 'SELECT * FROM private_wall.user WHERE id = %(userid)s;'
    data = { "userid" : session["userid"] }
    user = mysql.query_db(query, data)
    
    mysql = connectToMySQL('private_wall')
    users = mysql.query_db('SELECT * FROM private_wall.user ORDER BY first_name')
    
    mysql = connectToMySQL('private_wall')
    messages = mysql.query_db(f'SELECT * FROM private_wall.message INNER JOIN private_wall.user ON message.sender_id=user.id WHERE receiver_id={session["userid"]} ORDER BY message.created_at DESC')
    
    mysql = connectToMySQL('private_wall')
    sent_count = mysql.query_db(f'SELECT COUNT(*) FROM private_wall.message WHERE sender_id={session["userid"]}')
    now = datetime.now()
    elapsed_times = {}
    received_count = 0
    for message in messages:
        received_count += 1
        temp =  now - message['created_at']
        if temp.days >= 1:
            if temp.days == 1:
                value = f'{temp.days} day ago'
            else:
                value = f'{temp.days} days ago'
        elif int(temp.seconds/3600) >= 1:
            if int(temp.seconds/3600) == 1:
                value = f'{int(temp.seconds/3600)} hour ago'
            else:
                value = f'{int(temp.seconds/3600)} hours ago'
        else:
            if int(temp.seconds/60) == 1:
                value = f'{int(temp.seconds/60)} minute ago'
            else:
                value = f'{int(temp.seconds/60)} minutes ago'
        elapsed_times.update({f"{message['id']}": value})
    return render_template("wall.html", logged_user=user, users=users, messages=messages, elapsed_times=elapsed_times, received=received_count, sent=sent_count[0]['COUNT(*)'])

@app.route('/process_message', methods=['POST'])
def process_message():
    if request.method == 'POST':
        if len(request.form["message"]) < 5:
            return jsonify({'error': '5 charactors are required', 'status': False}) 
        else:
            mysql = connectToMySQL('private_wall')
            query = 'INSERT INTO private_wall.message (content, sender_id, receiver_id, created_at, updated_at) '\
                    'VALUES (%(message)s, %(sender_id)s, %(receiver_id)s, NOW(), NOW())'
            data = { 
                "message" : request.form["message"], 
                "sender_id" : session["userid"], 
                "receiver_id" : request.form["receiver_id"], 
            }
            new_message = mysql.query_db(query, data)
    
            mysql = connectToMySQL('private_wall')
            sent_count = mysql.query_db(f'SELECT COUNT(*) AS count FROM private_wall.message WHERE sender_id={session["userid"]}')
            return jsonify({'count': sent_count[0]['count'], 'success': 'sent successfully', 'status': True})

@app.route('/delete_message/<int:message_id>')
def delete_message(message_id):
    mysql = connectToMySQL('private_wall')
    query = 'DELETE FROM private_wall.message WHERE id=%(message_id)s'
    data = { 
        "message_id" : message_id, 
    }
    new_message = mysql.query_db(query, data)
    
    mysql = connectToMySQL('private_wall')
    received_count = mysql.query_db(f'SELECT COUNT(*) AS count FROM private_wall.message INNER JOIN private_wall.user ON message.sender_id=user.id WHERE receiver_id={session["userid"]} ORDER BY message.created_at DESC')
    return jsonify({'r_count': received_count[0]['count']})

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route("/username", methods=['POST'])
def username():
    found = False
    mysql = connectToMySQL('private_wall')
    query = "SELECT username from private_wall.user WHERE username = %(user)s;"
    data = { 'user': request.form['username'] }
    result = mysql.query_db(query, data)
    if result:
        found = True
    return render_template('partial/username.html', found=found) 

@app.route("/usersearch")
def search():
    mysql = connectToMySQL("private_wall")
    query = "SELECT * FROM private_wall.user WHERE username LIKE %%(name)s;"
    data = {
        "name" : request.args.get('name') + "%"
    }
    results = mysql.query_db(query, data)
    if request.args.get('name') == '':
        results = []
    return render_template("partial/search.html", users = results)

if __name__=="__main__":
    app.run(debug=True)