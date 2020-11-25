import mysql.connector as connector
class BLOOD:
    def __init__(self):
        self.con=connector.connect(host='localhost',port=3306,user='root',password='Manju@123',database='blood_donation')
        query='create table if not exists bloodbank (id int AUTO_INCREMENT PRIMARY KEY,donar_name varchar(20),date varchar(10),gender varchar(10),age int,blood_group varchar(20),location varchar(50),quantity float)'
        cur=self.con.cursor()
        cur.execute(query)
        print('Created')

    def insert_query(self,donor_name,date,gender,age,blood_group,location,quantity):
        query="insert into bloodbank(donar_name,date,gender,age,blood_group,location,quantity) values ('{}','{}','{}',{},'{}','{}',{})".format(donor_name,date,gender,age,blood_group,location,quantity)
        cur=self.con.cursor()
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
        
