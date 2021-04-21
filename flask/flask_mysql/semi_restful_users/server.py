from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route("/users")
def index():
    mysql = connectToMySQL('users')
    users = mysql.query_db('SELECT * FROM user;')
    return render_template("index.html", users=users)

@app.route("/users/new")
def new_user():
    return render_template("create.html")

@app.route("/users/create", methods=["POST"])
def create():
    mysql = connectToMySQL('users')
    query = 'INSERT INTO user (first_name, last_name, email, created_at, updated_at, description)'\
            'VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW(), %(description)s)'
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'description': request.form['description'],
    }
    new_user = mysql.query_db(query, data)

    return redirect('/users')

@app.route("/users/<int:pk>")
def show_user(pk):
    mysql = connectToMySQL('users')
    query = 'SELECT * FROM user WHERE user_id=%(pk)s;'
    data = {
        'pk': pk,
    }
    user = mysql.query_db(query, data)
    print(user)
    return render_template("show_user.html", user=user)

@app.route("/users/<int:pk>/edit")
def edit_user(pk):
    mysql = connectToMySQL('users')
    query = 'SELECT * FROM user WHERE user_id=%(pk)s;'
    data = {
        'pk': pk,
    }
    user = mysql.query_db(query, data)
    print(user)
    return render_template("edit.html", user=user)

@app.route("/users/<int:pk>/update", methods=["POST"])
def update(pk):
    mysql = connectToMySQL('users')
    query = 'UPDATE user SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW(), description=%(description)s'\
            'WHERE user_id=%(pk)s;'
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'description': request.form['description'],
        'pk': pk,
    }
    update_user = mysql.query_db(query, data)

    return redirect(f'/users/{pk}')

@app.route("/users/<int:pk>/destroy")
def destroy(pk):
    mysql = connectToMySQL('users')
    query = 'DELETE FROM user WHERE user_id=%(pk)s;'
    data = {
        'pk': pk,
    }
    destroy_user = mysql.query_db(query, data)

    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)