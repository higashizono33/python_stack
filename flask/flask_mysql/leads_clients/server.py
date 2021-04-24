from flask import Flask, render_template, redirect, request, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route("/")
def index():
    if 'start_date' and 'end_date' not in session:
        mysql = connectToMySQL('lead_gen_business')
        results = mysql.query_db('SELECT clients.first_name, clients.last_name, COUNT(*) AS count FROM lead_gen_business.leads '\
        'LEFT JOIN lead_gen_business.sites ON leads.site_id=sites.site_id '\
        'LEFT JOIN lead_gen_business.clients ON sites.client_id=clients.client_id GROUP BY clients.client_id ORDER BY count DESC;')
    else:
        start_date = session['start_date']
        end_date = session['end_date']
        mysql = connectToMySQL('lead_gen_business')
        results = mysql.query_db('SELECT clients.first_name, clients.last_name, COUNT(*) AS count FROM lead_gen_business.leads '\
        'LEFT JOIN lead_gen_business.sites ON leads.site_id=sites.site_id LEFT JOIN lead_gen_business.clients ON sites.client_id=clients.client_id '\
        f'WHERE registered_datetime BETWEEN "{start_date}" AND "{end_date}" GROUP BY clients.client_id ORDER BY count DESC;')
    return render_template("index.html", results=results)

@app.route("/filter_date", methods=['POST'])
def filter_date():
    if request.method == 'POST':
        session['start_date'] = request.form['start_date']
        session['end_date'] = request.form['end_date']
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)