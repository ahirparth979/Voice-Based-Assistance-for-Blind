'''
Created on Oct 23, 2020

@author: Parth Ahir
'''


import sqlite3

def create_user_table():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user(email TEXT PRIMARY KEY NOT NULL, password TEXT NOT NULL, pin INTEGER NOT NULL)")
    conn.commit()
    conn.close()

def insert_user(email, password, pin):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    #cur.execute("SELECT email FROM user")
    #email_exists = cur.fetchall()
    #print(email_exists)
    #print(email)
    #if not(email in email_exists):
    #    print('hiii')
    cur.execute("INSERT INTO user (email, password, pin) VALUES(?,?,?)",(email, password, pin))
    conn.commit()
    conn.close()

def view_user():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_user(email):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM user WHERE email=?",(email,))
    conn.commit()
    conn.close()

create_user_table()
#insert_user('ahirparth979@gmail.com', 'ajqjspnblrrgsmid', 1234)
#insert_user('ahir.umed@gmail.com', 'aa', 1234)
#delete_user('ahirparth979@gmail.com')
#delete_user('ahir.umed@gmail.com')
print(view_user())


##########################################################################


def create_receiver_table():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS receiver(email TEXT PRIMARY KEY NOT NULL)")
    conn.commit()
    conn.close()

def insert_receiver(email):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO receiver VALUES(?)",(email,))
    conn.commit()
    conn.close()

def view_receiver():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM receiver")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_receiver(email):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM receiver WHERE email=?",(email,))
    conn.commit()
    conn.close()
    
create_receiver_table()
insert_receiver('ahirparth979@gmail.com')
insert_receiver('ahir.umed@gmail.com')
#delete_receiver('ahir.umed@gmail.com')
print(view_receiver())