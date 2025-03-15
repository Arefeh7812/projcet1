import sqlite3
class Database1:
    def __init__(self,db_name):
        self.con=sqlite3.connect(db_name)
        self.cur=self.con.cursor()
        self.cur.execute('''
                         CREATE TABLE IF NOT EXISTS users id INTEGER PRIMARYKEYAUTOINCREMENT" 
                         Fname TEXT ,Lname TEXT ,email TEXT, password TEXT ''')
        self.con.commit()
    def insert(self,fname,lname,email,password):
        self.cur.execute("INSERT INTO users(fname,lname,email, password)VALUES(?,?,?,?)",
                       (fname,lname,email,password ) )
        self.con.commit()

    def find_users(self,email,password):
        self.cur.execute("SELECT fname,lname FRPM users WHERE email=?",(email,password))
        return self.cur.fetchone()
    