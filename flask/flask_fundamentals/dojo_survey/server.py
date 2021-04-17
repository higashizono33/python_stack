from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    radio_button = request.form['radio_button']
    check_box = request.form['check_box']
    return render_template("result.html", name=name, location=location, language=language, comment=comment, radio_button=radio_button, check_box=check_box)

if __name__=="__main__":
    app.run(debug=True)
