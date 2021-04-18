from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

# counter = 0
# visit = 0

@app.route('/')
def index():
    # global counter, visit
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    if 'visit' not in session:
        session['visit'] = 1
    else:
        session['visit'] += 1

    return render_template("index.html")

@app.route('/count_by2')
def counter_by2():
    session['counter'] += 1
    return redirect('/')

@app.route('/count_by_order', methods=['POST'])
def counter_by_order():
    session['counter'] += int(request.form['order']) - 1
    return redirect('/')

@app.route('/destroy')
def destroy_session():
    session.pop('counter')
    session.pop('visit')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)