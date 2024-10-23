import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="9686715002",database="second_db")
c=mydb.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS second_db")
c.execute("""CREATE TABLE if not exists customers(name varchar(50))""")
mydb.connect()
mydb.close()
c.execute("SHOW DATABASES")
for db in c:
    print(db)