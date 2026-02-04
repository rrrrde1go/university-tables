from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/tables/<int:day>')
def tables(day):
    return render_template('tables.html', day=day)

@app.route('/pdf/<int:day>')
def pdf_view(day):
    return render_template('pdf.html', day=day)

if __name__ == '__main__':
    app.run(debug=True)
