from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from flask import render_template
import datetime


def generate_pdf(day, tables_data, cutoff, stats, raw_tables_data, cutoff_history={}):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    pm = 0  # ПМ
    ivt = 0  # ИВТ
    itss = 0  # ИТСС
    ib = 0  # ИБ

    pm_places = 40
    ivt_places = 50
    itss_places = 30
    ib_places = 20

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


    if day >= 4:

        # Для PM
        if pm1 + pm2 + pm3 + pm4 > 0:
            pmpr1 = int(pm_places * (pm1 / pm)) if pm > 0 else 0
            pmpr2 = int(pm_places * (pm2 / pm)) if pm > 0 else 0
            pmpr3 = int(pm_places * (pm3 / pm)) if pm > 0 else 0
            pmpr4 = pm_places - (pmpr1 + pmpr2 + pmpr3)  # Остаток

        # Для IVT
        if ivt1 + ivt2 + ivt3 + ivt4 > 0:
            ivtpr1 = int(ivt_places * (ivt1 / ivt)) if ivt > 0 else 0
            ivtpr2 = int(ivt_places * (ivt2 / ivt)) if ivt > 0 else 0
            ivtpr3 = int(ivt_places * (ivt3 / ivt)) if ivt > 0 else 0
            ivtpr4 = ivt_places - (ivtpr1 + ivtpr2 + ivtpr3)

        # Для ITSS
        if itss1 + itss2 + itss3 + itss4 > 0:
            itsspr1 = int(itss_places * (itss1 / itss)) if itss > 0 else 0
            itsspr2 = int(itss_places * (itss2 / itss)) if itss > 0 else 0
            itsspr3 = int(itss_places * (itss3 / itss)) if itss > 0 else 0
            itsspr4 = itss_places - (itsspr1 + itsspr2 + itsspr3)

        # Для IB
        if ib1 + ib2 + ib3 + ib4 > 0:
            ibpr1 = int(ib_places * (ib1 / ib)) if ib > 0 else 0
            ibpr2 = int(ib_places * (ib2 / ib)) if ib > 0 else 0
            ibpr3 = int(ib_places * (ib3 / ib)) if ib > 0 else 0
            ibpr4 = ib_places - (ibpr1 + ibpr2 + ibpr3)
    else:
        pm_applicants = []
        ivt_applicants = []
        itss_applicants = []
        ib_applicants = []

        for applicant in tables_data:
            total_points = applicant.get("total_points", 0)
            faculty = applicant.get("faculty", "")


            priority = None
            for i in range(1, 5):
                if applicant.get(f"priority{i}") == 1:
                    if faculty == "PM": priority = i
                    break
                elif applicant.get(f"priority{i}") == 2:
                    if faculty == "IVT": priority = i
                    break
                elif applicant.get(f"priority{i}") == 3:
                    if faculty == "ITSS": priority = i
                    break
                elif applicant.get(f"priority{i}") == 4:
                    if faculty == "IB": priority = i
                    break

            if priority and total_points >= cutoff.get(faculty, 0):
                if faculty == "PM":
                    pm_applicants.append((total_points, priority, applicant))
                elif faculty == "IVT":
                    ivt_applicants.append((total_points, priority, applicant))
                elif faculty == "ITSS":
                    itss_applicants.append((total_points, priority, applicant))
                elif faculty == "IB":
                    ib_applicants.append((total_points, priority, applicant))


        pm_applicants.sort(key=lambda x: (-x[0], x[1]))
        ivt_applicants.sort(key=lambda x: (-x[0], x[1]))
        itss_applicants.sort(key=lambda x: (-x[0], x[1]))
        ib_applicants.sort(key=lambda x: (-x[0], x[1]))

        pm_to_enroll = min(pm_places, len(pm_applicants))
        ivt_to_enroll = min(ivt_places, len(ivt_applicants))
        itss_to_enroll = min(itss_places, len(itss_applicants))
        ib_to_enroll = min(ib_places, len(ib_applicants))

        pm_enrolled = pm_applicants[:pm_to_enroll]
        ivt_enrolled = ivt_applicants[:ivt_to_enroll]
        itss_enrolled = itss_applicants[:itss_to_enroll]
        ib_enrolled = ib_applicants[:ib_to_enroll]
        for points, priority, applicant in pm_enrolled:
            if priority == 1:
                pmpr1 += 1
            elif priority == 2:
                pmpr2 += 1
            elif priority == 3:
                pmpr3 += 1
            elif priority == 4:
                pmpr4 += 1

        for points, priority, applicant in ivt_enrolled:
            if priority == 1:
                ivtpr1 += 1
            elif priority == 2:
                ivtpr2 += 1
            elif priority == 3:
                ivtpr3 += 1
            elif priority == 4:
                ivtpr4 += 1

        for points, priority, applicant in itss_enrolled:
            if priority == 1:
                itsspr1 += 1
            elif priority == 2:
                itsspr2 += 1
            elif priority == 3:
                itsspr3 += 1
            elif priority == 4:
                itsspr4 += 1

        for points, priority, applicant in ib_enrolled:
            if priority == 1:
                ibpr1 += 1
            elif priority == 2:
                ibpr2 += 1
            elif priority == 3:
                ibpr3 += 1
            elif priority == 4:
                ibpr4 += 1

    if y_pos < 250:
        c.showPage()
        y_pos = height - 50

    y_pos -= 30

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
    headers = ["", "PM", "IVT", "ITSS", "IB"]
    for i, header in enumerate(headers):
        c.drawString(col_x_positions[i], y_pos, header)
    y_pos -= 15

    c.line(col_x_positions[0], y_pos, col_x_positions[4] + col_other_width, y_pos)
    y_pos -= 20

    # Строка 1: Общее кол-во заявлений
    c.drawString(col_x_positions[0], y_pos, "Total amount of applications")
    c.drawString(col_x_positions[1], y_pos, str(pm))
    c.drawString(col_x_positions[2], y_pos, str(ivt))
    c.drawString(col_x_positions[3], y_pos, str(itss))
    c.drawString(col_x_positions[4], y_pos, str(ib))
    y_pos -= 20

    # Строка 2: Количество мест на ОП
    c.drawString(col_x_positions[0], y_pos, "Number of places on OP")
    c.drawString(col_x_positions[1], y_pos, str(pm_places))
    c.drawString(col_x_positions[2], y_pos, str(ivt_places))
    c.drawString(col_x_positions[3], y_pos, str(itss_places))
    c.drawString(col_x_positions[4], y_pos, str(ib_places))
    y_pos -= 20

    # Строка 3: Кол-во заявлений 1-го приоритета
    c.drawString(col_x_positions[0], y_pos, "amount of applications 1-st priority")
    c.drawString(col_x_positions[1], y_pos, str(pm1))
    c.drawString(col_x_positions[2], y_pos, str(ivt1))
    c.drawString(col_x_positions[3], y_pos, str(itss1))
    c.drawString(col_x_positions[4], y_pos, str(ib1))
    y_pos -= 20

    # Заявлений 2-го приоритета
    c.drawString(col_x_positions[0], y_pos, "amount of applications 2-st priority")
    c.drawString(col_x_positions[1], y_pos, str(pm2))
    c.drawString(col_x_positions[2], y_pos, str(ivt2))
    c.drawString(col_x_positions[3], y_pos, str(itss2))
    c.drawString(col_x_positions[4], y_pos, str(ib2))
    y_pos -= 20

    # Заявлений 3-го приоритета
    c.drawString(col_x_positions[0], y_pos, "amount of applications 3-st priority")
    c.drawString(col_x_positions[1], y_pos, str(pm3))
    c.drawString(col_x_positions[2], y_pos, str(ivt3))
    c.drawString(col_x_positions[3], y_pos, str(itss3))
    c.drawString(col_x_positions[4], y_pos, str(ib3))
    y_pos -= 20

    # Заявлений 4-го приоритета
    c.drawString(col_x_positions[0], y_pos, "amount of applications 4-st priority")
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
    c.drawString(col_x_positions[0], y_pos, "Amount of enrolled by priority:")
    y_pos -= 20
    c.setFont("Helvetica", 9)

    # Зачисленные по приоритетам
    c.drawString(col_x_positions[0], y_pos, "With 1-st priority")
    c.drawString(col_x_positions[1], y_pos, str(pmpr1))
    c.drawString(col_x_positions[2], y_pos, str(ivtpr1))
    c.drawString(col_x_positions[3], y_pos, str(itsspr1))
    c.drawString(col_x_positions[4], y_pos, str(ibpr1))
    y_pos -= 20

    c.drawString(col_x_positions[0], y_pos, "With 2-nd priority")
    c.drawString(col_x_positions[1], y_pos, str(pmpr2))
    c.drawString(col_x_positions[2], y_pos, str(ivtpr2))
    c.drawString(col_x_positions[3], y_pos, str(itsspr2))
    c.drawString(col_x_positions[4], y_pos, str(ibpr2))
    y_pos -= 20

    c.drawString(col_x_positions[0], y_pos, "With 3-rd priority")
    c.drawString(col_x_positions[1], y_pos, str(pmpr3))
    c.drawString(col_x_positions[2], y_pos, str(ivtpr3))
    c.drawString(col_x_positions[3], y_pos, str(itsspr3))
    c.drawString(col_x_positions[4], y_pos, str(ibpr3))
    y_pos -= 20

    c.drawString(col_x_positions[0], y_pos, "With 4-th priority")
    c.drawString(col_x_positions[1], y_pos, str(pmpr4))
    c.drawString(col_x_positions[2], y_pos, str(ivtpr4))
    c.drawString(col_x_positions[3], y_pos, str(itsspr4))
    c.drawString(col_x_positions[4], y_pos, str(ibpr4))
    y_pos -= 20
    c.setFont("Helvetica-Bold", 9)
    c.drawString(col_x_positions[0], y_pos, "TOTAL enrolled:")
    total_pm = pmpr1 + pmpr2 + pmpr3 + pmpr4
    total_ivt = ivtpr1 + ivtpr2 + ivtpr3 + ivtpr4
    total_itss = itsspr1 + itsspr2 + itsspr3 + itsspr4
    total_ib = ibpr1 + ibpr2 + ibpr3 + ibpr4
    c.drawString(col_x_positions[1], y_pos, str(total_pm))
    c.drawString(col_x_positions[2], y_pos, str(total_ivt))
    c.drawString(col_x_positions[3], y_pos, str(total_itss))
    c.drawString(col_x_positions[4], y_pos, str(total_ib))
    y_pos -= 20
    c.setFont("Helvetica", 9)
    c.drawString(col_x_positions[0], y_pos, "Free places:")
    free_pm = max(0, pm_places - total_pm)
    free_ivt = max(0, ivt_places - total_ivt)
    free_itss = max(0, itss_places - total_itss)
    free_ib = max(0, ib_places - total_ib)

    c.drawString(col_x_positions[1], y_pos, str(free_pm))
    c.drawString(col_x_positions[2], y_pos, str(free_ivt))
    c.drawString(col_x_positions[3], y_pos, str(free_itss))
    c.drawString(col_x_positions[4], y_pos, str(free_ib))

    y_pos -= 20

    # Статус заполнения (без цвета)
    c.setFont("Helvetica", 9)
    c.drawString(col_x_positions[0], y_pos, "Status:")

    if day >= 4:
        status_pm = "FULL" if free_pm == 0 else f"{free_pm} left"
        status_ivt = "FULL" if free_ivt == 0 else f"{free_ivt} left"
        status_itss = "FULL" if free_itss == 0 else f"{free_itss} left"
        status_ib = "FULL" if free_ib == 0 else f"{free_ib} left"
    else:
        status_pm = f"{free_pm} free"
        status_ivt = f"{free_ivt} free"
        status_itss = f"{free_itss} free"
        status_ib = f"{free_ib} free"

    c.drawString(col_x_positions[1], y_pos, status_pm)
    c.drawString(col_x_positions[2], y_pos, status_ivt)
    c.drawString(col_x_positions[3], y_pos, status_itss)
    c.drawString(col_x_positions[4], y_pos, status_ib)

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer