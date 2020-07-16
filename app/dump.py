import mysql.connector
from mysql.connector import errorcode
from datetime import date


mydb = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        passwd = "Password@123",
        auth_plugin = "mysql_native_password",
        database = "YGMDB")

mycur = mydb.cursor()
"""
def renewal_date_check():
        condition = 10
        ids = []
        mycur.execute("select Station_ID, File_Date from Hopper_File_History")
        data = mycur.fetchall()
        today = date.today()
        for tuples in data:
                delta = today - tuples[1]
                if delta.days <= condition:        
                        ids.append(tuples[0])
        return ids
#delta = date.today() - data[0]
#if delta.days == 10:
#print(data)

"""
mycur.execute("select * from Master_Bank")
users = mycur.fetchall()
print(users)

list_labels = ["Bank_code", "Bank_Name", "Bank_Acc_Details", "Address", "Miscelleneous"]
items = []
for each_element in users:
        print(each_element)
"""
for i in list_labels, users:
        print(i)
        

zipobj = zip(list_labels,users)
dictionary = dict(zipobj)
"""
print(len(users))
for each_element in users:
        out = dict()
        out[list_labels[0]]=each_element[0]
        out[list_labels[1]]=each_element[1]
        out[list_labels[2]]=each_element[2]
        out[list_labels[3]]=each_element[3]
        out[list_labels[4]]=each_element[4]
        items.append(out)
print(items)

items = [dict(name='Name1', description='Description1'),
         dict(name='Name2', description='Description2'),
         dict(name='Name3', description='Description3')]
print(items)