from flask import Flask, render_template
import math
app = Flask(__name__)                     
    
@app.route('/')                           
def index():
    return render_template('index.html')  

@app.route('/<int:x>')                           
def index_2(x):
    if x%2 == 0:
        odd = False
        row = x
    else:
        odd = True
        if x == 1:
            row = 1
        else:
            row = x-1
    return render_template('index.html', row=row, odd=odd)  

@app.route('/<int:x>/<int:y>')                           
def index_3(x, y):
    if y%2 == 0:
        odd = False
        col = int(y/2)
    else:
        odd = True
        if y == 1:
            col = 'first_col'
        else:
            col = math.floor(y/2)
    return render_template('index.html', row=x, col=col, odd=odd)  

@app.route('/<int:x>/<int:y>/<color1>/<color2>')                           
def index_4(x, y, color1, color2):
    color_set = True
    if y%2 == 0:
        odd = False
        col = int(y/2)
    else:
        odd = True
        if y == 1:
            col = 'first_col'
        else:
            col = math.floor(y/2)
    return render_template('index.html', row=x, col=col, odd=odd, color_set=color_set, color1=color1, color2=color2)  
    
if __name__=="__main__":
    app.run(debug=True)                   
