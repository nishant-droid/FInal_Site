from app.mysqlconnection import DBConnection


class Interface(object):
    
    def __init__(self):
        self.connection = None
        self.my_cursor = None
        
        
    def create_connection(self, username, password):
        try:
            dbObject = DBConnection()
            self.connection = dbObject.connection(username, password)
            self.my_cursor = self.connection.cursor()
            return self.my_cursor

        except ConnectionError as ex:
            return False
    
    def create_cursor(self):
        if self.connection:
            self.get_connection()
            return self.connection.cursor()
    

    def get_connection(self):
        return self.connection
        
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            return True

        


        

    
        

