class Queries():

    def db_selection(self):
        query = "use YGMDB"
        return query

    def push_file(self):
        query = "load data local infile '/home/nishant/Documents/try/shared_code/app/static/uploads/Hopper.csv' into table Hopper_File_History fields terminated by ',' lines terminated by '\n'"
        return query
    
    def add_data(self, branchcode, branchname, atmcode, bankcode, bankadd, email, emailgroup):
        query = f"insert into YGMDB.Master_Branch(Branch_Code, Branch_Name, ATM_Code, Bank_Code, Bank_Address, Email, Email_Group) values('{branchcode}','{branchname}','{atmcode}','{bankcode}','{bankadd}','{email}','{emailgroup}')"
        return query