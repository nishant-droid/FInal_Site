class Queries():

    def db_selection(self):
        query = "use YGMDB"
        return query

    def push_file(self):
        query = "load data local infile '/home/nishant/Documents/try/shared_code/app/static/uploads/Hopper.csv' into table Hopper_File_History fields terminated by ',' lines terminated by '\n'"
        return query