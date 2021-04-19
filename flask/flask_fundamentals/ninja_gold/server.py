from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def index():
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if 'attempt' not in session:
        session['attempt'] = 1
    else:
        session['attempt'] += 1
    if session['attempt'] < 15:
        if request.method == 'POST':
            if request.form.get('farm'):
                money = random.randint(10, 20)
                ct = datetime.now().strftime('%Y-%m-%d %I:%M %p')
                activity = f'<li class=text-success>Ninja earned {money} golds from Farm {ct}</li>'
                session['activities'].insert(0, activity)
            if request.form.get('cave'):
                money = random.randint(5, 10)
                ct = datetime.now().strftime('%Y-%m-%d %I:%M %p')
                activity = f'<li class=text-success>Ninja earned {money} golds from Cave {ct}</li>'
                session['activities'].insert(0, activity)
            if request.form.get('house'):
                money = random.randint(2, 5)
                ct = datetime.now().strftime('%Y-%m-%d %I:%M %p')
                activity = f'<li class=text-success>Ninja earned {money} golds from House {ct}</li>'
                session['activities'].insert(0, activity)
            if request.form.get('casino'):
                money = random.randint(-50, 50)
                ct = datetime.now().strftime('%Y-%m-%d %I:%M %p')
                if money >= 0:
                    activity = f'<li class=text-success>Ninja earned {money} golds from Casino {ct}</li>'
                    session['activities'].insert(0, activity)
                else:
                    activity = f'<li class=text-danger>Ninja lost {money*-1} golds from Casino {ct}</li>'
                    session['activities'].insert(0, activity)
            if 'money' not in session:
                session['money'] = money
            else:
                session['money'] += money
    else:
        if session['money'] >= 500:
            session['result'] = 'won'
        else:
            session['result'] = 'lost'
    return redirect('/')

@app.route('/reset_money')
def reset_money():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)