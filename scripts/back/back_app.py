from flask import Flask, jsonify
from table_tools.check_tables import TableManager

app = Flask(__name__)
tm = TableManager(tables_dir="C:/Users/rrrrd/PycharmProjects/university-tables/tables")

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
