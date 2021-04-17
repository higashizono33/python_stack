from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html")

@app.route('/play/<int:times>')
def index_2(times):
    return render_template("index.html", times = times)

@app.route('/play/<int:times>/<color>')
def index_3(times, color):
    return render_template("index.html", times = times, color=color)

if __name__=="__main__":
    app.run(debug=True)