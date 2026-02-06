from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from flask import render_template
import datetime

def generate_pdf(day, tables_data, cutoff, stats, cutoff_history={}):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y_pos = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y_pos, f"Отчёт — День {day}")
    y_pos -= 25
    c.setFont("Helvetica", 10)
    c.drawString(50, y_pos, f"Дата формирования: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    y_pos -= 30

    # Проходные баллы
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Проходные баллы:")
    y_pos -= 15
    c.setFont("Helvetica", 10)
    for fac, val in cutoff.items():
        c.drawString(60, y_pos, f"{fac}: {val}")
        y_pos -= 12
    y_pos -= 20

    # Таблица абитуриентов
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Абитуриенты:")
    y_pos -= 15
    c.setFont("Helvetica", 8)

    # Заголовки
    headers = ["ФИО", "Факультет", "Специальность", "Общ. баллы",
               "Согласие", "Приоритет 1", "Приоритет 2", "Приоритет 3", "Приоритет 4"]
    x_positions = [50, 150, 220, 300, 360, 420, 470, 520, 570]
    for i, header in enumerate(headers):
        c.drawString(x_positions[i], y_pos, header)
    y_pos -= 12

    # Строки таблицы
    for row in tables_data:
        if y_pos < 50:
            c.showPage()
            y_pos = height - 50
        values = [
            row.get("fio", ""), row.get("faculty", ""), row.get("specialty", ""),
            str(row.get("total_points", "")), str(row.get("agreed", "")),
            str(row.get("priority1", "")), str(row.get("priority2", "")),
            str(row.get("priority3", "")), str(row.get("priority4", ""))
        ]
        for i, val in enumerate(values):
            c.drawString(x_positions[i], y_pos, val)
        y_pos -= 12

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer
