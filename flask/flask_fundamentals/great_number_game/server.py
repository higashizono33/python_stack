from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'answer' not in session:
        session['answer'] = random.randint(1, 100)
    return render_template("index.html")

@app.route('/check', methods=['POST'])
def check():
    if 'attempt' not in session:
        session['attempt'] = 1
    elif session['attempt'] > 3:
        return redirect('/lose')
    else:    
        session['attempt'] += 1

    if session['answer'] > int(request.form['number']):
        session['low'] = True
        session['high'] = False
    elif session['answer'] < int(request.form['number']):
        session['low'] = False
        session['high'] = True
    else:
        session['low'] = False
        session['high'] = False
        session['correct'] = True
    return redirect('/')

@app.route('/replay')
def replay():
    session.clear()
    return redirect('/')

@app.route('/lose')
def lose():
    session.clear()
    return render_template("lose.html")

@app.route('/board', methods=['POST'])
def show_board():
    attempt_num = session['attempt']
    session['name'] = request.form['name']
    session.clear()
    return render_template("leaderboard.html", attempt_num=attempt_num)

if __name__=="__main__":
    app.run(debug=True)