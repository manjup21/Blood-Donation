import mysql.connector as connector
class BLOOD:
    def __init__(self):
        self.con=connector.connect(host='localhost',port=3306,user='root',password='Manju@123',database='blood_donation')
        query='create table if not exists bloodbank (date varchar(10),donar_name varchar(20),blood_group varchar(6),gender varchar(10),adress varchar(50),quantity float)'
        cur=self.con.cursor()
        cur.execute(query)
        print('Created')
    def insert_query(self,date,donar_name,blood_group,gender,adress,quantity):
        query="insert into bloodbank values ('{}','{}','{}','{}','{}',{})".format(date,donar_name,blood_group,gender,adress,quantity)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Inserted")
    def get_info(self):
        query='select * from bloodbank'
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
    def patient(self,blood_group):
        query="select * from bloodbank where blood_group= '{}'".format(blood_group)
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
        

helper=BLOOD()
#helper.insert_query('2018-09-28','Manjunath P','B +ve','Male','Karnataka',2.5)
#helper.get_info()
helper.patient('B +ve')