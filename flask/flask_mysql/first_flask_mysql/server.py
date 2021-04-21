from flask import Flask, render_template
from mysqlconnection import connectToMySQL # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('friends')
    users = mysql.query_db('SELECT * FROM users;')  # call the query_db function, pass in the query as a string
    print(users)
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
