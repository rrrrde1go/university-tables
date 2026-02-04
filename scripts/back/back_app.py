from flask import Flask, render_template, jsonify
from table_tools.db_table_manager import TableManager

app = Flask(__name__)
tm = TableManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tables/<int:day>')
def tables(day):
    tm.load_day(day)
    tables_data = tm.tables
    cutoff = tm.calculate_cutoff()
    stats = tm.get_statistics()
    return render_template('tables.html', day=day, tables=tables_data, cutoff=cutoff, stats=stats)

@app.route('/pdf/<int:day>')
def pdf_view(day):
    tm.load_day(day)
    cutoff = tm.calculate_cutoff()
    stats = tm.get_statistics()
    return render_template('pdf.html', day=day, cutoff=cutoff, stats=stats)

@app.route('/api/tables/<int:day>')
def api_tables(day):
    tm.load_day(day)
    return jsonify(tm.tables)

@app.route('/api/stats/<int:day>')
def api_stats(day):
    tm.load_day(day)
    return jsonify({
        "cutoff": tm.calculate_cutoff(),
        "stats": tm.get_statistics()
    })

if __name__ == '__main__':
    app.run(debug=True)
