import mysql.connector as connector
import random
class BLOOD:
    def __init__(self):
        self.con=connector.connect(host='localhost',port=3306,user='root',password='Manju@123',database='blood_donation')
        query='create table if not exists bloodbank (id int AUTO_INCREMENT PRIMARY KEY,donar_name varchar(20),date varchar(10),gender varchar(10),age int,blood_group varchar(20),location varchar(50),quantity float)'
        query1='create table if not exists blood_loc(blood_id int,blood_group varchar(20),quant float,locate varchar(50),foreign key (blood_id) references bloodbank(id))'
        query2='create table if not exists accept_info(id int AUTO_INCREMENT PRIMARY KEY,acceptor_name varchar(20),location varchar(50),blood_group varchar(20),phone_no varchar(20),amount_blood int)'
        cur=self.con.cursor()
        cur.execute(query)
        cur.execute(query1)
        cur.execute(query2)
        print('Created')

    def insert_query(self,donor_name,date,gender,age,blood_group,location,quantity):
        query="insert into bloodbank(donar_name,date,gender,age,blood_group,location,quantity) values ('{}','{}','{}',{},'{}','{}',{})".format(donor_name,date,gender,age,blood_group,location,quantity)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        query="select id from bloodbank where donar_name='{}'".format(donor_name)
        cur=self.con.cursor()
        cur.execute(query)
        li=[]
        for id_val in cur:
            li.append(id_val)
        query="insert into blood_loc values ({},'{}',{},'{}')".format(int(li[0][0]),blood_group,quantity,location)
        cur.execute(query)
        self.con.commit()
        print("Inserted")

    def get_by_location(self,locate):
        query="select * from bloodbank where location='{}'".format(locate)
        cur=self.con.cursor()
        cur.execute(query)
        li=[]
        for row in cur:
            li.append(row)
        return li

    def get_by_location_group(self,group,loc):
        query="select blood_group,sum(quant) from blood_loc where blood_group='{}' and  locate='{}'".format(group,loc)
        cur=self.con.cursor()
        cur.execute(query)
        li=[]
        for row in cur:
            li.append(row)
        return li
    def add_accept_info(self,name,loc,blood_group,phone_num,amount):
        query="insert into accept_info(acceptor_name,location,blood_group,phone_no,amount_blood) values ('{}','{}','{}','{}',{})".format(name,loc,blood_group,phone_num,amount)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
    def delete_from_bank(self,blood_group,location,quantity):
        query="select blood_id from blood_loc where blood_group='{}' and locate='{}'".format(blood_group,location)
        cur=self.con.cursor()
        cur.execute(query)
        li=[]
        for row in cur:
            li.append(row)
        print(li)
        li1=[li[i][0] for i in range(len(li))]
        print(li1)
        de=random.sample(li1,int(quantity))
        print(de)
        for value in de:
            query="delete from blood_loc where blood_id={}".format(value)
            cur=self.con.cursor()
            cur.execute(query)
            self.con.commit()
    
    def get_by_group(self,group):
        query="select blood_group,sum(quant),locate from blood_loc where blood_group='{}' group by locate;".format(group)
        cur=self.con.cursor()
        cur.execute(query)
        li=[]
        for row in cur:
            li.append(row)
        return li
           
        

    def get_info(self):
        query='select * from bloodbank'
        cur=self.con.cursor()
        cur.execute(query)
        li=[]
        for row in cur:
            li.append(row)
        return li

    def patient(self,blood_group):
        query="select blood_group,location from bloodbank where blood_group= '{}'".format(blood_group)
        cur=self.con.cursor()
        cur.execute(query)
        li=[]
        for row in cur:
            li.append(row)
        return li
        
# h=BLOOD()
# h.insert_query('ABC','blal','male',12,'blall','ooo',1)