import sqlite3 as lite
import sys

#------------------------
# создание скл файла

connect = None

try:
    connect = lite.connect('test.db')
    cur = connect.cursor()
except lite.Error as e:
    print(f"Error {e.args[0]}:")
    #sys.exit(1)

#------------------------
# создание скл таблицы

#cur.execute('CREATE TABLE cars (id INT, name TEXT, price INT)')

#------------------------
# заполнение  скл таблицы

cur.execute("INSERT INTO cars VALUES(?,?,?)",(1,'BMW',10000))
cur.execute("INSERT INTO cars VALUES(2,'AMG',9000)")

sp=[[3,'Audi',9500],[4,'WAG',8000]]

for car in sp:
    cur.execute("INSERT INTO cars VALUES(?,?,?)", (car[0],car[1],car[2]))

# ------------------------
# вывод данных  скл таблицы

sql_select_query = """SELECT * from cars"""
cur.execute(sql_select_query)

record = cur.fetchall()

print(len(record))

for i in record :
    print(i)


