import mysql.connector
from mysql.connector import errorcode


class DBConnection(object):
    def __init__(self):
        self.mydb = None
        self.my_cursor = None
        

    def connection(self, user, pwd):
        try:
            mydb = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    passwd = "Password@123",
                    auth_plugin = "mysql_native_password",)
                
            if mydb.is_connected:
                return mydb

        except mysql.connector.Error as err:
            return False
        
"""
    def DBCursor(self):
        if self.connection != False:
            my_cursor = self.connection.cursor()
            return my_cursor
        else:
            return False
"""
