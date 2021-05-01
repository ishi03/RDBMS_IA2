from impl2 import *
import sqlite3

conn = sqlite3.connect('coordinates.db')
cursor = conn.cursor()
print ("Opened database successfully\n")
cursor.execute("select name from coordinates")
conn.commit()
data = cursor.fetchall()
searchq=input("Enter bulding name to search: ")

prob=exec(data,searchq)

cursor.execute("create table results(result_name varchar(100),distance float,probability float)")
conn.commit()
query="insert into results (result_name,distance,probability) values (?,?,?)"
cursor.executemany(query,prob)
conn.commit()
t=input("\ncheck point, enter any key to continue...")
cursor.execute("drop table results")
conn.close()