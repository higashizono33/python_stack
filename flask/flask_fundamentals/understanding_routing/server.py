from flask import Flask
app = Flask(__name__)  

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def call_dojo():
    return 'Dojo!'

@app.route('/say/<word>')
def say_word(word):
    return f'Hi! {word}'

@app.route('/repeat/<int:times>/<word>')
def repeat_word(times, word):
    repeated = ''
    print(times)
    for i in range(0, times):
        repeated += f'{word}/'
    return repeated

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return 'Sorry! No response. Try again.', 404

if __name__=="__main__":
    app.run(debug=True)
