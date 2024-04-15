import sqlite3
def canector(path):
    con=sqlite3.connect(path)
    cur=con.cursor()
    return con,cur
def selectdeta(con,cur):
    cur.execute("SELECT name,age FROM employee WHERE age=13")
    return cur.fetchall()
con,cur=canector("mydatabase4.db")
deta=selectdeta(con,cur)
print(deta)