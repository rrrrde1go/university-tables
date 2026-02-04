from flask import Flask, render_template
#создаём веб приложение
app = Flask(__name__)


#Главная страница. Здесь происходит выбор дня
@app.route('/')
def index():
    return render_template('index.html')


#страница таблиц для конкретного дня с номером day
@app.route('/tables/<int:day>')
def tables(day):
    return render_template('tables.html', day=day)


#страница с пдфниками каждого дня
@app.route('/pdf/<int:day>')
def pdf_view(day):
    return render_template('pdf.html', day=day)

if __name__ == '__main__':
    app.run(debug=True)
