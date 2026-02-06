from flask import Flask, render_template, request, send_file
from table_tools.db_table_manager import TableManager
from table_tools.pdf_generator import generate_pdf

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tables")
def tables():
    day = int(request.args.get("day", 1))
    tm = TableManager()
    tm.load_day(day)

    tm.cursor.execute("""
        SELECT fio, faculty, specialty, total_points, agreed,
               priority1, priority2, priority3, priority4,
               physics, russian, math, individual
        FROM students WHERE day=?
    """, (day,))
    rows = tm.cursor.fetchall()

    tables_data = []
    for r in rows:
        tables_data.append({
            "fio": r[0],
            "faculty": r[1],
            "specialty": r[2],
            "total_points": r[3],
            "agreed": r[4],
            "priority1": r[5],
            "priority2": r[6],
            "priority3": r[7],
            "priority4": r[8],
            "physics": r[9],
            "russian": r[10],
            "math": r[11],
            "individual": r[12]
        })

    cutoff = tm.calculate_cutoff()

    raw_stats = tm.get_statistics()
    stats = {}
    for fac, s in raw_stats.items():
        if isinstance(s, dict):
            stats[fac] = {
                "total": s.get("total", 0),
                "priorities": s.get("priorities", {1:0,2:0,3:0,4:0})
            }
        else:
            # Если s — число, то приводим к дефолтной структуре
            stats[fac] = {
                "total": s,
                "priorities": {1:0,2:0,3:0,4:0}
            }

    tm.close()

    return render_template("tables.html",
                           day=day,
                           tables=tables_data,
                           cutoff=cutoff,
                           stats=stats)

@app.route("/pdf")
def pdf_view():
    day = int(request.args.get("day", 1))
    tm = TableManager()
    tm.load_day(day)

    tm.cursor.execute("""
        SELECT fio, faculty, specialty, total_points, agreed,
               priority1, priority2, priority3, priority4,
               physics, russian, math, individual
        FROM students WHERE day=?
    """, (day,))
    rows = tm.cursor.fetchall()

    tables_data = []
    for r in rows:
        tables_data.append({
            "fio": r[0],
            "faculty": r[1],
            "specialty": r[2],
            "total_points": r[3],
            "agreed": r[4],
            "priority1": r[5],
            "priority2": r[6],
            "priority3": r[7],
            "priority4": r[8],
            "physics": r[9],
            "russian": r[10],
            "math": r[11],
            "individual": r[12]
        })

    cutoff = tm.calculate_cutoff()

    raw_stats = tm.get_statistics()
    stats = {}
    for fac, s in raw_stats.items():
        if isinstance(s, dict):
            stats[fac] = {
                "total": s.get("total", 0),
                "priorities": s.get("priorities", {1:0,2:0,3:0,4:0})
            }
        else:
            stats[fac] = {
                "total": s,
                "priorities": {1:0,2:0,3:0,4:0}
            }

    tm.close()

    pdf_file = generate_pdf(day, tables_data, cutoff, stats, cutoff_history={})
    return send_file(pdf_file,
                     download_name=f"report_day_{day}.pdf",
                     as_attachment=True,
                     mimetype='application/pdf')


if __name__ == "__main__":
    app.run(debug=True)
