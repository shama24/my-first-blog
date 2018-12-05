import sqlite3
 
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()
 
sql = """SELECT * FROM auth.User;"""
 
n = cursor.execute(sql)
print(n)
conn.commit()