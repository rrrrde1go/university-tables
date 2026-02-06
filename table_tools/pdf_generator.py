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

    # Заголовки направлений
    headers1 = ['PM:', 'IVT:', 'ITSS:', 'IB:']
    x_positions = [50, 175, 305, 435]
    for i, header in enumerate(headers1):
        c.drawString(x_positions[i], y_pos, header)
    y_pos -= 12

    y_save = y_pos

    # Заголовки
    headers = ["ФИО", "Общ. баллы"]
    x_positions = [45, 120]
    for i, header in enumerate(headers):
        c.drawString(x_positions[i], y_pos, header)
    y_pos -= 12

    # Строки таблицы PM
    for row in tables_data:
        spec = row.get("faculty", "")
        if y_pos < 50:
            c.showPage()
            y_pos = height - 50
        if spec == 'PM':
            values = [
                row.get("fio", ""), str(row.get("total_points", ""))
            ]
            for i, val in enumerate(values):
                c.drawString(x_positions[i], y_pos, val)
            y_pos -= 12

    y_pos = y_save

    # Заголовки
    headers = ["ФИО", "Общ. баллы"]
    x_positions = [175, 250]
    for i, header in enumerate(headers):
        c.drawString(x_positions[i], y_pos, header)
    y_pos -= 12

    for row in tables_data:
        spec = row.get("faculty", "")
        if y_pos < 50:
            c.showPage()
            y_pos = height - 50
        if spec == 'IVT':
            values = [
                row.get("fio", ""), str(row.get("total_points", ""))
            ]
            for i, val in enumerate(values):
                c.drawString(x_positions[i], y_pos, val)
            y_pos -= 12

    y_pos = y_save

    # Заголовки
    headers = ["ФИО", "Общ. баллы"]
    x_positions = [305, 380]
    for i, header in enumerate(headers):
        c.drawString(x_positions[i], y_pos, header)
    y_pos -= 12

    for row in tables_data:
        spec = row.get("faculty", "")
        if y_pos < 50:
            c.showPage()
            y_pos = height - 50
        if spec == 'ITSS':
            values = [
                row.get("fio", ""), str(row.get("total_points", ""))
            ]
            for i, val in enumerate(values):
                c.drawString(x_positions[i], y_pos, val)
            y_pos -= 12

    y_pos = y_save

    # Заголовки
    headers = ["ФИО", "Общ. баллы"]
    x_positions = [435, 510]
    for i, header in enumerate(headers):
        c.drawString(x_positions[i], y_pos, header)
    y_pos -= 12

    for row in tables_data:
        spec = row.get("faculty", "")
        if y_pos < 50:
            c.showPage()
            y_pos = height - 50
        if spec == 'IB':
            values = [
                row.get("fio", ""), str(row.get("total_points", ""))
            ]
            for i, val in enumerate(values):
                c.drawString(x_positions[i], y_pos, val)
            y_pos -= 12


    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer
