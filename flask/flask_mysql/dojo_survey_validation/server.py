from flask import Flask, render_template, request, flash, redirect, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    mysql = connectToMySQL('dojo_survey')
    locations = mysql.query_db('SELECT * FROM dojo_survey.location;')
    mysql = connectToMySQL('dojo_survey')
    languages = mysql.query_db('SELECT * FROM dojo_survey.language;')
    return render_template("index.html", locations=locations, languages=languages)

@app.route('/post', methods=['POST'])
def post():
    if len(request.form['name']) < 1:
        flash("Please enter a first name")
    if len(request.form['comment']) > 120:
        flash("Please enter comment less than 120 letters")
    if len(request.form['location']) < 2:
        if request.form['new_location']:
            if len(request.form['new_location']) < 2:
                flash("location should be at least 2 characters")
            else:
                mysql = connectToMySQL('dojo_survey')
                query = 'INSERT INTO dojo_survey.location (name, created_at, updated_at)'\
                        'VALUES (%(location_name)s, NOW(), NOW())'
                data = {
                    'location_name': request.form['new_location'],
                }
                new_location = mysql.query_db(query, data)
                entered_location = True
        else:
            flash("Location should be at least 2 characters")
    if len(request.form['language']) < 2:
        if request.form['new_language']:
            if len(request.form['new_language']) < 2:
                flash("language should be at least 2 characters")
            else:
                mysql = connectToMySQL('dojo_survey')
                query = 'INSERT INTO dojo_survey.language (name, created_at, updated_at)'\
                        'VALUES (%(language_name)s, NOW(), NOW())'
                data = {
                    'language_name': request.form['new_language'],
                }
                new_language = mysql.query_db(query, data)
                entered_language = True
        else:
            flash("Language should be at least 2 characters")

    if not '_flashes' in session.keys():
        mysql = connectToMySQL('dojo_survey')
        query = 'INSERT INTO dojo_survey.post (name, comment, created_at, updated_at, location_id, language_id)'\
                'VALUES (%(name)s, %(comment)s, NOW(), NOW(), (SELECT location_id FROM dojo_survey.location WHERE name=%(location)s),'\
                '(SELECT language_id FROM dojo_survey.language WHERE name=%(language)s))'
        if entered_location:
            location = request.form['new_location']
        else:
            location = request.form['location']
        if entered_language:
            language = request.form['new_language']
        else:
            language = request.form['language']
        data = {
            'name': request.form['name'],
            'comment': request.form['comment'],
            'location': location,
            'language': language,
        }
        new_post = mysql.query_db(query, data)
        return redirect('/result')
    else:
        return redirect('/')

@app.route('/result')
def result():
    mysql = connectToMySQL('dojo_survey')
    last_post = mysql.query_db('SELECT * FROM dojo_survey.post WHERE post_id=(SELECT MAX(post_id) FROM dojo_survey.post);')
    mysql = connectToMySQL('dojo_survey')
    location = mysql.query_db(f'SELECT name FROM dojo_survey.location WHERE location_id={last_post[0]["location_id"]};')
    mysql = connectToMySQL('dojo_survey')
    language = mysql.query_db(f'SELECT name FROM dojo_survey.language WHERE language_id={last_post[0]["language_id"]};')
    return render_template("result.html", post=last_post, location=location, language=language)

if __name__=="__main__":
    app.run(debug=True)
