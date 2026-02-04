import mysql.connector
import pandas as pd
import os

DB_CONFIG = {
    'user': 'root',
    'password': 'WreckaKrew!2026Mys',
    'host': '127.0.0.1',
    'database': 'university',
    'port': 3307
}

TABLES_DIR = "../tables"

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students")

cursor.execute("""
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    day INT,
    fio VARCHAR(255),
    faculty VARCHAR(100),
    specialty VARCHAR(100),
    total_points INT,
    agreed INT,
    priority1 INT,
    priority2 INT,
    priority3 INT,
    priority4 INT
)
""")

for day in range(1, 5):
    for faculty_file in os.listdir(TABLES_DIR):
        if faculty_file.endswith(f"{day}.xlsx"):
            file_path = os.path.join(TABLES_DIR, faculty_file)
            try:
                df = pd.read_excel(file_path)
            except Exception as e:
                print(f"[ERROR] {e}")
                continue

            df = df.rename(columns={
                'ФИО': 'fio',
                'Факультет': 'faculty',
                'Направление': 'specialty',
                'Сумма баллов': 'total_points',
                'Согласовано': 'agreed',
                'Приоритет 1': 'priority1',
                'Приоритет 2': 'priority2',
                'Приоритет 3': 'priority3',
                'Приоритет 4': 'priority4'
            })

            for _, row in df.iterrows():
                cursor.execute("""
                    INSERT INTO students
                    (day, fio, faculty, specialty, total_points, agreed, priority1, priority2, priority3, priority4)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    day,
                    row.get('fio', ''),
                    row.get('faculty', ''),
                    row.get('specialty', ''),
                    row.get('total_points', 0),
                    row.get('agreed', 0),
                    row.get('priority1', 0),
                    row.get('priority2', 0),
                    row.get('priority3', 0),
                    row.get('priority4', 0)
                ))

conn.commit()
cursor.close()
conn.close()
print("Заполнение базы завершено!")
