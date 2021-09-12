import sqlite3
db=sqlite3.connect("regis.db")
cr=db.cursor()
cr.execute("create table regis(Uname text,Email text,Password)")
db.commit()
db.close()
print("table create")