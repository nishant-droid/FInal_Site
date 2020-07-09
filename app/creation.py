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

mycursor.execute("create table if not exists YGMDB.Master_Branch( Branch_Code varchar(20) primary key,"
                  "Branch_Name varchar(50),"
                  "ATM_Code varchar(20), Bank_Code varchar(20), Bank_Address text, Email varchar(50), Email_Group int)")

mycursor.execute("create table if not exists YGMDB.Master_CIT(CIT_Code varchar(20) primary key,"
                  "CIT_Name varchar(50),"
                  "Bank_Account_Details varchar(20), Address text, Contact_Person_Name varchar(20), Contact_Person_Mobile_Number int, Contact_Person_Email varchar(25))")

mycursor.execute("create table if not exists YGMDB.Master_Bank(Bank_Code varchar(20) primary key,"
                  "Bank_Name varchar(50),"
                  "Bank_Account_Details varchar(20), Address text, Miscellaneous text)")

mycursor.execute("create table if not exists YGMDB.Master_MFT(MFT_ID varchar(20) primary key,"
                  "Site_Name varchar(25),"
                  "District varchar(20), Bank_Code int, Branch_Code int, CIT_Name varchar(20), CIT_Code varchar(20), Cassette_Configuration varchar(5), Cash_Live_Date date, Tech_Live_Date date, UBS_Code varchar(20),"
                  "Route_Number varchar(5),Sequence_Number varchar(20), ATM_Serial_Number int, Secretary_Name varchar(20), Secretary_Number int, Engineer_Name varchar(20), Engineer_Number int,"
                  "Cash_Removal_Date date, Cash_Removal_Reason varchar(20), Closure_Type varchar(10), Closure_Date date, Closure_Remark tinytext, Salary_Payment_Date date, Est_Salary_per_Payment int)")

mycursor.execute("create table if not exists YGMDB.Insurance(MFT_ID varchar(20),Status bool, Insurance_Commence_Date date, Insurence_Renewal_Date date, Insurance_Amount int)")

mycursor.execute("create table if not exists YGMDB.Cassette_Configuration(Machine_Capacity int, Model varchar(20), 100_Denomination bool default 0, 200_Denomination bool default 0, 500_Denomination bool default 0, 2000_Denomination bool default 0)")