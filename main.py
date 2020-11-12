from flask import Flask,render_template,request,url_for,redirect
#from flask_bootstrap import Bootstrap
from My_Sql_data import BLOOD

app=Flask(__name__)
#Bootstrap(app)

helper=BLOOD()

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/donate',methods=["POST","GET"])
def donate():
    if request.method=="POST":
        name=request.form['name']
        date=request.form['Date']
        gender=request.form['gender']
        group=request.form['groups']
        location=request.form['location']
        quantity=request.form['quant']
        age=request.form['age']
        return redirect(url_for('thanks'))
    else:
        return render_template('donate.html')

@app.route('/checking')
def checking():
    return render_template('result.html')

@app.route('/bloodbank')
def bloodbank():
    return render_template('bloodbank.html')

@app.route('/thanks')
def thanks():
    return render_template('thankyou.html')



if __name__=='__main__':
    app.run(debug=True)