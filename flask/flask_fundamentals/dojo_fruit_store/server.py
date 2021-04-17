from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    context = {
        'apple': int(request.form['apple']),
        'strawberry': int(request.form['strawberry']),
        'raspberry': int(request.form['raspberry']),
        # 'backberry': request.form['backberry'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'student_id': request.form['student_id'],
        'count': int(request.form['apple'])+int(request.form['strawberry'])+int(request.form['raspberry']),
    }
    # when refreshed this page, posted same data again 
    return render_template("checkout.html", context=context)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    