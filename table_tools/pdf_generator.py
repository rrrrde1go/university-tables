from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from flask import render_template
import datetime


def generate_pdf(day, tables_data, cutoff, stats, raw_tables_data, cutoff_history={}):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Инициализация переменных для подсчета статистики
    # Общее количество заявлений по направлениям
    pm = 0  # ПМ
    ivt = 0  # ИВТ
    itss = 0  # ИТСС
    ib = 0  # ИБ

    # Количество мест на ОП (из таблицы в изображении)
    pm_places = 40
    ivt_places = 50
    itss_places = 30
    ib_places = 20

    # Заявлений по приоритетам (первые цифры)
    pm1 = 0
    pm2 = 0
    pm3 = 0
    pm4 = 0

    ivt1 = 0
    ivt2 = 0
    ivt3 = 0
    ivt4 = 0

    itss1 = 0
    itss2 = 0
    itss3 = 0
    itss4 = 0

    ib1 = 0
    ib2 = 0
    ib3 = 0
    ib4 = 0

    # Зачисленные по приоритетам (pr - прошедшие)
    pmpr1 = 0
    pmpr2 = 0
    pmpr3 = 0
    pmpr4 = 0

    ivtpr1 = 0
    ivtpr2 = 0
    ivtpr3 = 0
    ivtpr4 = 0

    itsspr1 = 0
    itsspr2 = 0
    itsspr3 = 0
    itsspr4 = 0

    ibpr1 = 0
    ibpr2 = 0
    ibpr3 = 0
    ibpr4 = 0

    y_pos = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y_pos, f"Report — Day {day}")
    y_pos -= 25
    c.setFont("Helvetica", 10)
    c.drawString(50, y_pos, f"Formation date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    y_pos -= 30

    # Проходные баллы
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Passing scores:")
    y_pos -= 15
    c.setFont("Helvetica", 10)
    for fac, val in cutoff.items():
        if len(str(val)) == 3:
            c.drawString(60, y_pos, f"{fac}: {val}")
            y_pos -= 12
        if len(str(val)) != 3:
            c.drawString(60, y_pos, f"{fac}: not enough")
            y_pos -= 12
    y_pos -= 20

    # Таблица абитуриентов
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Applicants:")
    y_pos -= 15
    c.setFont("Helvetica", 8)

    # Заголовки направлений
    headers1 = ['PM:', 'IVT:', 'ITSS:', 'IB:']
    x_positions = [45, 175, 305, 435]
    for i, header in enumerate(headers1):
        c.drawString(x_positions[i], y_pos, header)
    y_pos -= 12

    y_save = y_pos

    # Заголовки
    headers = ["ID:", "total points:"]
    x_positions = [45, 120]
    for i, header in enumerate(headers):
        c.drawString(x_positions[i], y_pos, header)
    y_pos -= 12

    m_y_pos = 60

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
        if m_y_pos > y_pos:
            m_y_pos = y_pos

    y_pos = y_save

    # Заголовки
    headers = ["ID:", "total points:"]
    x_positions = [175, 250]
    for i, header in enumerate(headers):
        c.drawString(x_positions[i], y_pos, header)
    y_pos -= 12

    # Строки таблицы IVT
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
        if m_y_pos > y_pos:
            m_y_pos = y_pos

    y_pos = y_save

    # Заголовки
    headers = ["ID:", "total points:"]
    x_positions = [305, 380]
    for i, header in enumerate(headers):
        c.drawString(x_positions[i], y_pos, header)
    y_pos -= 12

    # Строки таблицы ITSS
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
        if m_y_pos > y_pos:
            m_y_pos = y_pos

    y_pos = y_save

    # Заголовки
    headers = ["ID:", "total points:"]
    x_positions = [435, 510]
    for i, header in enumerate(headers):
        c.drawString(x_positions[i], y_pos, header)
    y_pos -= 12

    # Строки таблицы IB
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
        if m_y_pos > y_pos:
            m_y_pos = y_pos

    y_pos = m_y_pos
    y_pos -= 20


    for raw_table in raw_tables_data:
        # Для приоритета 1
        if raw_table.get("priority1") == 1:
            pm1 += 1
            pm += 1
        if raw_table.get("priority1") == 2:
            pm2 += 1
            pm += 1
        if raw_table.get("priority1") == 3:
            pm3 += 1
            pm += 1
        if raw_table.get("priority1") == 4:
            pm4 += 1
            pm += 1

        # Для приоритета 2
        if raw_table.get("priority2") == 1:
            ivt1 += 1
            ivt += 1
        if raw_table.get("priority2") == 2:
            ivt2 += 1
            ivt += 1
        if raw_table.get("priority2") == 3:
            ivt3 += 1
            ivt += 1
        if raw_table.get("priority2") == 4:
            ivt4 += 1
            ivt += 1

        # Для приоритета 3
        if raw_table.get("priority3") == 1:
            itss1 += 1
            itss += 1
        if raw_table.get("priority3") == 2:
            itss2 += 1
            itss += 1
        if raw_table.get("priority3") == 3:
            itss3 += 1
            itss += 1
        if raw_table.get("priority3") == 4:
            itss4 += 1
            itss += 1

        # Для приоритета 4
        if raw_table.get("priority4") == 1:
            ib1 += 1
            ib += 1
        if raw_table.get("priority4") == 2:
            ib2 += 1
            ib += 1
        if raw_table.get("priority4") == 3:
            ib3 += 1
            ib += 1
        if raw_table.get("priority4") == 4:
            ib4 += 1
            ib += 1

    # Подсчет зачисленных
    for applicant in tables_data:
        if applicant.get("priority1") == 1:
            pmpr1 += 1
        if applicant.get("priority1") == 2:
            pmpr2 += 1
        if applicant.get("priority1") == 3:
            pmpr3 += 1
        if applicant.get("priority1") == 4:
            pmpr4 += 1

        if applicant.get("priority2") == 1:
            ivtpr1 += 1
        if applicant.get("priority2") == 2:
            ivtpr2 += 1
        if applicant.get("priority2") == 3:
            ivtpr3 += 1
        if applicant.get("priority2") == 4:
            ivtpr4 += 1

        if applicant.get("priority3") == 1:
            itsspr1 += 1
        if applicant.get("priority3") == 2:
            itsspr2 += 1
        if applicant.get("priority3") == 3:
            itsspr3 += 1
        if applicant.get("priority3") == 4:
            itsspr4 += 1

        if applicant.get("priority4") == 1:
            ibpr1 += 1
        if applicant.get("priority4") == 2:
            ibpr2 += 1
        if applicant.get("priority4") == 3:
            ibpr3 += 1
        if applicant.get("priority4") == 4:
            ibpr4 += 1

    if y_pos < 250:
        c.showPage()
        y_pos = height - 50

    y_pos -= 30

    # Создание таблицы
    c.setFont("Helvetica", 9)


    available_width = width - 60



    col1_width = available_width * 0.75
    col_other_width = available_width * 0.0625

    col_x_positions = [
        30,
        30 + col1_width,
        30 + col1_width + col_other_width,
        30 + col1_width + 2 * col_other_width,
        30 + col1_width + 3 * col_other_width
    ]

    # Заголовок таблицы
    headers = ["", "ПМ", "ИВТ", "ИТСС", "ИБ"]
    for i, header in enumerate(headers):
        c.drawString(col_x_positions[i], y_pos, header)
    y_pos -= 15


    c.line(col_x_positions[0], y_pos, col_x_positions[4] + col_other_width, y_pos)
    y_pos -= 20

    # Строка 1: Общее кол-во заявлений
    c.drawString(col_x_positions[0], y_pos, "Общее кол-во заявлений")
    c.drawString(col_x_positions[1], y_pos, str(pm))
    c.drawString(col_x_positions[2], y_pos, str(ivt))
    c.drawString(col_x_positions[3], y_pos, str(itss))
    c.drawString(col_x_positions[4], y_pos, str(ib))
    y_pos -= 20

    # Строка 2: Количество мест на ОП
    c.drawString(col_x_positions[0], y_pos, "Количество мест на ОП")
    c.drawString(col_x_positions[1], y_pos, str(pm_places))
    c.drawString(col_x_positions[2], y_pos, str(ivt_places))
    c.drawString(col_x_positions[3], y_pos, str(itss_places))
    c.drawString(col_x_positions[4], y_pos, str(ib_places))
    y_pos -= 20

    # Строка 3: Кол-во заявлений 1-го приоритета
    c.drawString(col_x_positions[0], y_pos, "Кол-во заявлений 1-го приоритета")
    c.drawString(col_x_positions[1], y_pos, str(pm1))
    c.drawString(col_x_positions[2], y_pos, str(ivt1))
    c.drawString(col_x_positions[3], y_pos, str(itss1))
    c.drawString(col_x_positions[4], y_pos, str(ib1))
    y_pos -= 20

    # Заявлений 2-го приоритета
    c.drawString(col_x_positions[0], y_pos, "Кол-во заявлений 2-го приоритета")
    c.drawString(col_x_positions[1], y_pos, str(pm2))
    c.drawString(col_x_positions[2], y_pos, str(ivt2))
    c.drawString(col_x_positions[3], y_pos, str(itss2))
    c.drawString(col_x_positions[4], y_pos, str(ib2))
    y_pos -= 20

    # Заявлений 3-го приоритета
    c.drawString(col_x_positions[0], y_pos, "Кол-во заявлений 3-го приоритета")
    c.drawString(col_x_positions[1], y_pos, str(pm3))
    c.drawString(col_x_positions[2], y_pos, str(ivt3))
    c.drawString(col_x_positions[3], y_pos, str(itss3))
    c.drawString(col_x_positions[4], y_pos, str(ib3))
    y_pos -= 20

    # Заявлений 4-го приоритета
    c.drawString(col_x_positions[0], y_pos, "Кол-во заявлений 4-го приоритета")
    c.drawString(col_x_positions[1], y_pos, str(pm4))
    c.drawString(col_x_positions[2], y_pos, str(ivt4))
    c.drawString(col_x_positions[3], y_pos, str(itss4))
    c.drawString(col_x_positions[4], y_pos, str(ib4))
    y_pos -= 25

    # Разделительная линия
    c.line(col_x_positions[0], y_pos, col_x_positions[4] + col_other_width, y_pos)
    y_pos -= 20

    # Заголовок для зачисленных
    c.setFont("Helvetica-Bold", 9)
    c.drawString(col_x_positions[0], y_pos, "Кол-во зачисленных по приоритетам:")
    y_pos -= 20
    c.setFont("Helvetica", 9)

    # Зачисленные по приоритетам
    c.drawString(col_x_positions[0], y_pos, "По 1-му приоритету")
    c.drawString(col_x_positions[1], y_pos, str(pmpr1))
    c.drawString(col_x_positions[2], y_pos, str(ivtpr1))
    c.drawString(col_x_positions[3], y_pos, str(itsspr1))
    c.drawString(col_x_positions[4], y_pos, str(ibpr1))
    y_pos -= 20
    c.drawString(col_x_positions[0], y_pos, "По 2-му приоритету")
    c.drawString(col_x_positions[1], y_pos, str(pmpr2))
    c.drawString(col_x_positions[2], y_pos, str(ivtpr2))
    c.drawString(col_x_positions[3], y_pos, str(itsspr2))
    c.drawString(col_x_positions[4], y_pos, str(ibpr2))
    y_pos -= 20
    c.drawString(col_x_positions[0], y_pos, "По 3-му приоритету")
    c.drawString(col_x_positions[1], y_pos, str(pmpr3))
    c.drawString(col_x_positions[2], y_pos, str(ivtpr3))
    c.drawString(col_x_positions[3], y_pos, str(itsspr3))
    c.drawString(col_x_positions[4], y_pos, str(ibpr3))
    y_pos -= 20
    c.drawString(col_x_positions[0], y_pos, "По 4-му приоритету")
    c.drawString(col_x_positions[1], y_pos, str(pmpr4))
    c.drawString(col_x_positions[2], y_pos, str(ivtpr4))
    c.drawString(col_x_positions[3], y_pos, str(itsspr4))
    c.drawString(col_x_positions[4], y_pos, str(ibpr4))
    y_pos -= 30

    # генерация итоговой таблицы ОТЧЁТА
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Итоговая статистика:")
    y_pos -= 15
    c.setFont("Helvetica", 8)

    # Заголовки
    headers = ["", "ПМ", "ИВТ", "ИТСС", "ИБ"]
    x_positions = [50, 120, 180, 240, 300]
    for i, header in enumerate(headers):
        c.drawString(x_positions[i], y_pos, header)
    y_pos -= 12

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer
