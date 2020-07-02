import mysql.connector
from datetime import date, datetime, time, timedelta

mydb = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    passwd = "Password@123",
                    auth_plugin = "mysql_native_password",)

mycur = mydb.cursor()

min_balance = 50000

mycur.execute("use YGMDB")
mycur.execute("select count(*) from Dummy")
count = mycur.fetchone()
mycur.execute(f"create temporary table temp_tbl_balance(select Station_ID,Total_Cash,File_Date,File_Time from Hopper_File_History order by Hopper_File_History.File_Date desc, Hopper_File_History.File_Time desc limit {count[0]})")
#mycur.execute(f"select Station_ID,Total_Cash from temp_tbl_balance where Total_Cash <={min_balance};")
mycur.execute("select * from temp_tbl")
temp = mycur.fetchall()
for i in temp:
    print(i)


