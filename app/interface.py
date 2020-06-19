from app.mysqlconnection import DBConnection

class Interface(object):
    
    def __init__(self):
        self.connection = None

    def create_connection(self, username, password):
        try:
            dbObject = DBConnection()
            self.connection = dbObject.connection(username, password)
            return True

        except ConnectionError as ex:
            return False

    def get_connection(self):   
        return self.connection

        

    
        

