from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('pets')
    pets = mysql.query_db('SELECT * FROM pets;')
    print(pets)
    return render_template("index.html", pets=pets)

@app.route("/create", methods=["POST"])
def create_pet():
    mysql = connectToMySQL('pets')
    # query = 'INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW())'
    # for sql injection attack
    query = f"INSERT INTO pets (name, type) VALUES ('{request.form['name']}', '{request.form['type']}')"
    # query = f"SELECT * FROM users WHERE email = '{request.form['email']}';"
    # data = {
    #     'name': request.form['name'],
    #     'type': request.form['type'],
    # }
    new_pet = mysql.query_db(query)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)