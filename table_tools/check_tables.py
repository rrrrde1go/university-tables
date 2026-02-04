import pandas as pd
import os

class TableManager:
    def __init__(self, tables_dir):
        self.tables_dir = tables_dir
        self.day = None
        self.tables = {}

    def load_day(self, day):
        self.day = day
        programs = ['PM', 'IVT', 'ITSS', 'IB']
        self.tables = {}
        for prog in programs:
            file_path = os.path.join(self.tables_dir, f"{prog.lower()}{day}.xlsx")
            if os.path.exists(file_path):
                df = pd.read_excel(file_path)
                self.tables[prog] = df.to_dict(orient='records')
            else:
                print(f"[WARNING] Файл не найден: {file_path}")
                self.tables[prog] = []

    def calculate_cutoff(self):
        cutoff = {}
        for prog, students in self.tables.items():
            agreed_students = [s for s in students if s.get("Наличие согласия")]
            agreed_students.sort(key=lambda x: x.get("Сумма баллов", 0), reverse=True)
            seats = {"PM":40, "IVT":50, "ITSS":30, "IB":20}[prog]
            if len(agreed_students) >= seats:
                cutoff[prog] = agreed_students[seats-1]["Сумма баллов"]
            else:
                cutoff[prog] = "НЕДОБОР"
        return cutoff

    def get_statistics(self):
        stats = {}
        for prog, students in self.tables.items():
            total = len(students)
            agreed = sum(1 for s in students if s.get("Наличие согласия"))
            priorities = {1:0,2:0,3:0,4:0}
            for s in students:
                pr = s.get("Приоритет")
                if pr in priorities:
                    priorities[pr] += 1
            stats[prog] = {"total": total, "agreed": agreed, "priorities": priorities}
        return stats
