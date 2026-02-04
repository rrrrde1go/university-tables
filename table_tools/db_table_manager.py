import mysql.connector

DB_CONFIG = {
    'user': 'root',
    'password': 'WreckaKrew!2026Mys',
    'host': '127.0.0.1',
    'database': 'university',
    'port': 3307
}

class TableManager:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)
        self.tables = []
        self.current_day = None

    def load_day(self, day):
        self.current_day = day
        self.cursor.execute(
            "SELECT * FROM students WHERE day=%s", (day,)
        )
        self.tables = self.cursor.fetchall()

    def calculate_cutoff(self):
        cutoff = {}
        faculties = set(row['faculty'] for row in self.tables)
        for fac in faculties:
            fac_rows = [r for r in self.tables if r['faculty'] == fac]
            if fac_rows:
                total_points = [r['total_points'] for r in fac_rows]
                cutoff[fac] = max(total_points)
            else:
                cutoff[fac] = 0
        return cutoff

    def get_statistics(self):
        stats = {}
        faculties = set(row['faculty'] for row in self.tables)
        for fac in faculties:
            fac_rows = [r for r in self.tables if r['faculty'] == fac]
            total = len(fac_rows)
            agreed = sum(r['agreed'] for r in fac_rows)
            priorities = {1:0,2:0,3:0,4:0}
            for r in fac_rows:
                for i in range(1,5):
                    priorities[i] += r.get(f'priority{i}', 0)
            stats[fac] = {'total': total, 'agreed': agreed, 'priorities': priorities}
        return stats

    def close(self):
        self.cursor.close()
        self.conn.close()
