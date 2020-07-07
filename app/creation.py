import mysql.connector

mydb = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    passwd = "Password@123",
                    auth_plugin = "mysql_native_password",)

mycursor = mydb.cursor()
"""
mycursor.execute("create database if not exists YGMDB")

mycursor.execute("create table if not exists YGMDB.Hopper_File_History(Station_ID varchar(10),Location varchar(30), "
                  "Hopper1_Count int,"
                  "Hopper1_Value int, Hopper2_Count int, Hopper2_Value int,"
                  "Hopper3_Count int, Hopper3_Value int,Hopper4_Count int, Hopper4_Value int,"
                  "Total_Cash int, File_Date date, File_Time Time)")

mycursor.execute("create table if not exists YGMDB.Log(User varchar(10), Activity (20), Previous_Data varchar(50), New_Data varchar(50), Date_Stamp timestamp default current_timestamp")
mycursor.execute("set time_zone=''+05:30")
"""

mycursor.execute("create table if not exists YGMDB.Master_Branch(Branch_Code varchar(20) primary key,"
                  "Branch_Name varchar(50),"
                  "ATM_Code varchar(20), Bank_Code varchar(20), Bank_Address text, Email varchar(50), Email_Group int)")
