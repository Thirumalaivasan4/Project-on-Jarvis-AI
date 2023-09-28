import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host="localhost",user="root",password="SQL123456789",database="jarvis")
if con:
    print("connected successfully")
else:
    print("problem in connecting!")
def insert(name,age,city):
    rs=con.cursor()
    sql="insert into demo (sname,age,city) values(%s,%s,%s)"
    user=(name,age,city)
    rs.execute(sql,user)
    con.commit()
    print("Inserted successfully!")
def update(id,name,age,city):
    rs=con.cursor()
    sql="update demo set sname=%s,age=%s,city=%s where id=%s"
    user=(name,age,city,id)
    rs.execute(sql,user)
    con.commit()
    print("updated successfully!")
def select():
    rs=con.cursor()
    sql="select id,sname,age,city from demo"
    rs.execute(sql)
    result=rs.fetchall()
    print(tabulate(result,headers=['ID','NAME','AGE','CITY']))
def delete(id):
    rs=con.cursor()
    sql="delete from demo where id=%s"
    user=(id,)
    rs.execute(sql,user)
    con.commit()
    print("Deleted successfully!")
while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.To Exit")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        name=input("Enter The Name: ")
        age=input("Enter The Age: ")
        city=input("Enter The City: ")
        insert(name,age,city)
    elif(ch==2):
        id=input("Enter the Id to be update: ")
        name=input("Enter The Name: ")
        age=input("Enter The Age: ")
        city=input("Enter The City: ")
        update(id,name,age,city)
    elif(ch==3):
        select()
    elif(ch==4):
        id=input("Enter The Record Id to be deleted: ")
        delete(id)
    elif(ch==5):
        quit()
    else:
        print("Please Enter The correct option. ")