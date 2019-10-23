#!/usr/bin/python
import MySQLdb
 
class Database: 
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",  # your host 
                            user="root",       # username
                            passwd="nugusha",     # password
                            db="pythonspot")   # name of the database
        
        # Create a Cursor object to execute queries.
        self.cur = self.db.cursor()
    
    def insert(self, data):
        command = "INSERT INTO data(speed, length, label) VALUES"
        for d in data:
            command += f"\n({d[0]},{d[1]},{d[2]}),"
        command = command[:-1] + ";"

        print(command)

        self.cur.execute(command)
        self.db.commit()
        
        # print the first and second columns
        #for row in self.cur.fetchall() :
        #    print (row[0], " ", row[1])
    
    def insertResult(self,coef1,coef2,result):
        command = "INSERT INTO results(coef1, coef2, result) VALUES "
        command += f"\n ({coef1},{coef2},{result});" 
        self.cur.execute(command)
        self.db.commit()
    
    def select(self):
        command = "SELECT * FROM data"
        self.cur.execute(command)
        records = self.cur.fetchall()

        return records