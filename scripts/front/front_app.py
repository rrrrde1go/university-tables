from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/tables/<int:day>')
def tables(day):
    if day not in [1, 2, 3, 4]:
        return 'Такого дня нет', 404
    return render_template('tables.html', day=day)

@app.route('/pdf')
def pdf_view():
    return render_template('pdf.html')

if __name__ == '__main__':
    app.run(debug=True)
