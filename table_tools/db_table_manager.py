import sqlite3
import pandas as pd
import os
from Constants import op_place_amount

class TableManager:
    def __init__(self, db_path="students.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table()

    # Создание пустой таблицы
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

    # Загрузка данных об абитуриентах на определённый день
    def load_day(self, day):
        self.cursor.execute("DELETE FROM students")
        self.conn.commit()
        excel_folder = os.path.join(os.path.dirname(__file__), "../tables")
        files = ["pm", "ivt", "itss", "ib"]
        for idx, faculty_file in enumerate(files):
            file_path = os.path.join(excel_folder, f"{faculty_file}{day}.xlsx")
            df = pd.read_excel(file_path)
            for _, row in df.iterrows():
                priorities = [0, 0, 0, 0]
                if row["Приоритет"] != 0:
                    priorities[idx] = int(row["Приоритет"])
                self.cursor.execute("SELECT 1 FROM students WHERE fio = ?",
                                    (row.get("ID"),))
                if self.cursor.fetchone() is not None:
                    self.cursor.execute(
                        f"UPDATE students SET priority{idx+1} = ? WHERE fio = ?",
                        (priorities[idx], row.get("ID"))
                    )
                else:
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

    # Расчёт проходного балла
    def calculate_cutoff(self):
        cutoff = {}
        op_names = ["PM", "IVT", "ITSS", "IB"]
        cutoff_points_list = {"PM": [], "IVT": [], "ITSS": [], "IB": []}
        self.cursor.execute(
            """SELECT fio, total_points, agreed,
               priority1, priority2, priority3, priority4,
               physics, russian, math, individual FROM students ORDER BY total_points DESC"""
        )
        rows = self.cursor.fetchall()
        for row in rows:
            if not row[2]:
                continue
            if all(len(cutoff_points_list[name]) == op_place_amount[name] for name in op_names):
                break
            total_points = row[1]
            priorities = [row[3], row[4], row[5], row[6]]
            for i in sorted(int(j) for j in priorities if int(j) != 0):
                op_name = op_names[priorities.index(i)]
                if len(cutoff_points_list[op_name]) < op_place_amount[op_name]:
                    cutoff_points_list[op_name].append(total_points)

        for name in op_names:
            if len(cutoff_points_list[name]) == op_place_amount[name]:
                cutoff[name] = cutoff_points_list[name][-1]
            else:
                cutoff[name] = "Недобор"

        return cutoff

    def filtered_students(self):
        pass

    def close(self):
        self.conn.close()
