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
        li=helper.get_by_location(loc)
        print(loc)
        print(li)
        if len(li)==0:
            return redirect(url_for('sorry',loc=loc))
        else:
            return render_template('show_info.html',li=li[::-1])
        #return "<h1>Success</h1>"
    else:
        return render_template('bloodbank.html')

@app.route('/sorry/<loc>')
def sorry(loc):
    return render_template('sorry.html',loc=loc)

@app.route('/<name>')
def thanks(name):
    return render_template('thankyou.html',name=name)

@app.route('/bloodneed',methods=['POST','GET'])
def bloodneed():
    if request.method=="POST":
        group=request.form['groups1']
        loc=request.form['location2']
        li=helper.get_by_location_group(group,loc)
        print(li)
        if li[0][0]==None or li[0][1]==None:
            return render_template('so_sad.html',group=group,loc=loc)
        else:
            print(type(li))
            return redirect(url_for('gotblood',li=li)) 
    else:
        return render_template('bloodneed.html')

@app.route('/so_sad',methods=['POST','GET'])
def others():
    if request.method=='POST':
        group=request.form['groups1']
        data=helper.get_by_group(group)
        print(data)
        return render_template("otheroptions.html",data=data)
    else:
        return render_template('searchblood.html')

@app.route('/gotblood/<li>',methods=["POST","GET"])
def gotblood(li):
    if request.method=="POST":
        name=request.form['name']
        loc=request.form['location']
        number=request.form['phone']
        quant=request.form['quantity']
        group=request.form['groups']
        helper.add_accept_info(name,loc,group,number,int(quant))
        helper.delete_from_bank(group,loc,quant)
        return render_template('afteraccept.html',name=name)
    else:
        num=int(li[16:17])
        return render_template('gotblood.html',li=li,num=num)


if __name__=='__main__':
    app.run(debug=True)