import sqlite3
db=sqlite3.connect("regis.db")
cr=db.cursor()
cr.execute("create table ins(ENroll text,Control text,Dastr text,Ulic text,Sensor text,Digital text)")
db.commit()
db.close()
print("table create")