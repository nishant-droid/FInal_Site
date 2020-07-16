#import things
from flask_table import Table, Col
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

# Declare your table
class ItemTable(Table):
    Bank_Code = Col('Bank Code')
    Bank
    description = Col('Description')

# Get some objects
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
"""
items = [Item('Name1', 'Description1'),
         Item('Name2', 'Description2'),
         Item('Name3', 'Description3')]
"""
# Or, equivalently, some dicts
items = [dict(name='Name1', description='Description1'),
         dict(name='Name2', description='Description2'),
         dict(name='Name3', description='Description3')]

# Or, more likely, load items from your database with something like
#items = ItemModel.query.all()
dbcur.execute(query.get_data("Master_Bank"))
data = dbcur.fetchall()
items=[]
list_labels = ["Bank_code", "Bank_Name", "Bank_Acc_Details", "Address", "Miscelleneous"]
for each_element in data:
    out = dict()
    out[list_labels[0]]=each_element[0]
    out[list_labels[1]]=each_element[1]
    out[list_labels[2]]=each_element[2]
    out[list_labels[3]]=each_element[3]
    out[list_labels[4]]=each_element[4]
    items.append(out)

# Populate the table
print(items)
table = ItemTable(items)

# Print the html
print(table.__html__())
# or just {{ table }} from within a Jinja template