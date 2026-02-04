import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="WreckaKrew!2026Mys",
    database="university",
    port=3307
)

print("Подключение успешно!")
conn.close()
