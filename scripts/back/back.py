import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='252526',
    port='3306',
    database='python_connect'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM users')

users = mycursor.fetchall()

for user in users:
    print(user)







