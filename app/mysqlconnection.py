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
                    user = user,
                    passwd = pwd,
                    auth_plugin = "mysql_native_password",)
            my_cursor = mydb.cursor()
            return my_cursor

        except mysql.connector.Error as err:
            return err
