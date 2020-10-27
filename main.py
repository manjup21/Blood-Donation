from flask import Flask,render_template
#from flask_bootstrap import Bootstrap
from My_Sql_data import BLOOD

app=Flask(__name__)
#Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/checking')
def checking():
    return render_template('result.html')

@app.route('/bloodbank')
def bloodbank():
    return render_template('bloodbank.html')


if __name__=='__main__':
    app.run(debug=True)