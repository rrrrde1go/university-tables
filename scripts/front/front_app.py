from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.route('/pdf')
def pdf_view():
    return render_template('pdf.html')

if __name__ == '__main__':
    app.run(debug=True)
