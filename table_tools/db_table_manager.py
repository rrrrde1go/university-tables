import sqlite3
import pandas as pd
import os

class TableManager:
    def __init__(self, db_path="students.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
        DROP TABLE IF EXISTS students
        """)
        self.cursor.execute("""
        CREATE TABLE students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day INTEGER,
            fio TEXT,
            faculty TEXT,
            specialty TEXT,
            total_points INTEGER,
            agreed INTEGER,
            priority1 INTEGER,
            priority2 INTEGER,
            priority3 INTEGER,
            priority4 INTEGER,
            physics INTEGER,
            russian INTEGER,
            math INTEGER,
            individual INTEGER
        )
        """)
        self.conn.commit()

    def load_day(self, day):
        excel_folder = os.path.join(os.path.dirname(__file__), "../tables")
        files = ["pm", "ivt", "itss", "ib"]
        for idx, faculty_file in enumerate(files):
            file_path = os.path.join(excel_folder, f"{faculty_file}{day}.xlsx")
            df = pd.read_excel(file_path)
            for _, row in df.iterrows():
                priorities = [0, 0, 0, 0]
                if row["Приоритет"] > 0:
                    priorities[idx] = int(row["Приоритет"])
                self.cursor.execute("""
                    INSERT INTO students (
                        day, fio, faculty, specialty, total_points, agreed,
                        priority1, priority2, priority3, priority4,
                        physics, russian, math, individual
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    day,
                    row.get("ID", ""),
                    faculty_file.upper(),
                    "",
                    row.get("Сумма баллов", 0),
                    int(row.get("Наличие согласия", 0)),
                    priorities[0],
                    priorities[1],
                    priorities[2],
                    priorities[3],
                    row.get("Балл Физика/ИКТ", 0),
                    row.get("Балл Русский язык", 0),
                    row.get("Балл Математика", 0),
                    row.get("Балл за индивидуальные достижения", 0)
                ))
        self.conn.commit()

    def get_statistics(self):
        stats = {}
        self.cursor.execute("SELECT faculty, COUNT(*) FROM students GROUP BY faculty")
        for faculty, count in self.cursor.fetchall():
            stats[faculty] = count
        return stats

    def calculate_cutoff(self):
        cutoff = {}
        for faculty in ["PM", "IVT", "ITSS", "IB"]:
            self.cursor.execute("""
                SELECT MAX(total_points) FROM students
                WHERE faculty=?
            """, (faculty,))
            val = self.cursor.fetchone()[0]
            cutoff[faculty] = val if val is not None else "НЕДОБОР"
        return cutoff

    def close(self):
        self.conn.close()
