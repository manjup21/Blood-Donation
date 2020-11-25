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

@app.route('/information')
def information():
    return render_template('information.html')

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
        helper.insert_query(name,date,gender,int(age),group,location,float(quantity))
        return redirect(url_for('thanks',name=name))
    else:
        return render_template('donate.html')

@app.route('/checking')
def checking():
    return render_template('result.html')

@app.route('/bloodbank',methods=["POST","GET"])
def bloodbank():
    if request.method=="POST":
        loc=request.form['location1']
        print(loc)
        return "<h1>Success</h1>"
        #blood_list=helper.get_info()
    else:
        return render_template('bloodbank.html')

@app.route('/<name>')
def thanks(name):
    return render_template('thankyou.html',name=name)



if __name__=='__main__':
    app.run(debug=True)