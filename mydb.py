import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'atonu',
    password = '1016',

)


#prepare a cursor object

coursorobject = database.cursor()


#create a database
coursorobject.execute("CREATE DATABASE crm")
print("ALL DOne!!")