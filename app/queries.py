class Queries():

    def db_selection(self):
        query = "use YGMDB"
        return query

    def push_file(self):
        query = "load data local infile '/home/nishant/Documents/try/shared_code/app/static/uploads/Hopper.csv' into table Hopper_File_History fields terminated by ',' lines terminated by '\n'"
        return query
    
    def add_data_branch(self, branchcode, branchname, atmcode, bankcode, bankadd, email, emailgroup):
        query = f"insert into YGMDB.Master_Branch(Branch_Code, Branch_Name, ATM_Code, Bank_Code, Bank_Address, Email, Email_Group) values('{branchcode}','{branchname}','{atmcode}','{bankcode}','{bankadd}','{email}','{emailgroup}')"
        return query

    def add_data_CIT(self, citcode, citname, bankaccdetails, add, contactpersonname, contactpersonnumber, contactpersonemail):
        query = f"insert into YGMDB.Master_CIT(CIT_Code, CIT_Name, Bank_Account_Details, Address, Contact_Person_Name, Contact_Person_Mobile_Number, Contact_Person_Email) values('{citcode}','{citname}','{bankaccdetails}','{add}','{contactpersonname}','{contactpersonnumber}','{contactpersonemail}')"
        return query
    
    def add_data_Bank(self, bankcode, bankname, bankaccdetails, add, miscellaneous):
        query = f"insert into YGMDB.Master_Bank(Bank_Code, Bank_Name, Bank_Account_Details, Address, Miscellaneous) values('{bankcode}','{bankname}','{bankaccdetails}','{add}','{miscellaneous}')"
        return query

    def add_data_MFT(self, mftif, sitename, district, bankcode, branchcode, citname, citcode, cassetteconfig, cashlivedate,techlivedate, ubscode, routenumber, sequencenumber, atmserialnumber,secretaryname, secretarynumber, engineername, engineernumber, cashremovaldate, cashremovalreason, closuretype, closuredate, closureremark, salarypaymentdate, salaryperpayment):
        query = f"insert into YGMDB.Master_Bank(MFT_ID, Site_Name, District, Bank_Code, Branch_Code, CIT_Name, CIT_Code, Cassette_Configuration, Cash_Live_Date, Tech_Live_Date, UBS_Code, Route_Number, Sequence_Number, ATM_Serial_Number, Secretary_Name, Secretary_Number, Engineer_Name, Engineer_Number, Cash_Removal_Date, Cash_Removal_Reason, Closure_Type, Closure_Date, Closure_Remark, Salary_Payment_Date, Est_Salary_per_Payment ) "
        "values('{mftid}','{sitename}','{district}','{bankcode}','{branchcode}','{citname}','{citcode}','{cassetteconfig}','{cashlivedate}','{techlivedate}','{ubscode}','{routenumber}', '{sequencenumber}','{atmserialnumber}','{secretaryname}', '{secretarynumber}', '{engineername}', '{engineernumber}', '{cashremovaldate}', '{cashremovalreason}', '{closuretype}', '{closuredate}', '{closureremark}', '{salarypaymentdate}', '{salaryperpayment}')"
        return query