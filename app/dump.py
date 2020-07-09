import mysql.connector
from mysql.connector import errorcode


mydb = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        passwd = "Password@123",
        auth_plugin = "mysql_native_password",)

mycur = mydb.cursor()

mycur.execute("use YGMDB")
mycur.execute("select current_user()")
data = mycur.fetchall()
user = data[0][0]
user = user.split("@")
print(user[0])
