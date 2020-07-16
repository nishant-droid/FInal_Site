from app.mysqlconnection import DBConnection
from app.file_handle import File_Handle
from app.tables import Master_Bank_Table


class Interface(object):
    
    def __init__(self):
        self.connection = None
        self.my_cursor = None
        self.file_manupilator = None
        self.file_check = None
        self.data = None
        
        
    def create_connection(self, username, password):
        try:
            print("Create connection was called")
            dbObject = DBConnection()
            self.connection = dbObject.connection(username, password)
            if not self.connection:
                return False
            else:
                self.my_cursor = self.connection.cursor()
            return self.my_cursor

        except ConnectionError as ex:
            return False
    
    def create_cursor(self):
        if self.connection:
            return self.connection.cursor()

    def commit_DB(self):
        if self.connection:
            return self.connection.commit()
    

    def get_connection(self):
        print('get connection was called')
        return self.connection
        
    
    def close_connection(self):
        if self.connection:
            print('Close connection was called after self.connection codition is true')
            self.connection.disconnect()
            self.connection = None
            return True
    
    def file_manupilation(self,filename,hopper_date,hopper_time):
        fileobject = File_Handle()
        self.file_manupilator = fileobject.File_Selection(filename,hopper_date,hopper_time)
        return True
    
    def check_file(self,hfile):
        fileobject = File_Handle()
        self.file_check = fileobject.File_check(hfile)
        if self.file_check:
            return self.file_check
        else:
            return False

    def get_data(self,data):
        masterbank = Master_Bank_Table(data, classes=['table table-striped'])
        return masterbank


    