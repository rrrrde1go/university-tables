import pandas as pd
import openpyxl as opx
import random


# Для удобства PM - 0; IVT - 1; ITSS - 2; IB - 3
class Student:
    def __init__(self, uid, priority_template):
        self.id = uid
        self.agreement: bool = bool(random.randint(0, 1))
        random.shuffle(priority_template)
        # Приоритет [0] - первый приоритет; [1] - второй приоритет и т. д.
        self.priority = priority_template
        # Баллы [0] - Физика; [1] - Русский; [2] - Математика; [3] - индивидуальные достижения
        self.scores = [random.randint(50, 100) for _ in range(3)] + [random.randint(0, 10)]


# Информация по количеству абитуриентов
total_amount = {'PM': [60, 380, 1000, 1240],
                'IVT': [100, 370, 1150, 1390],
                'ITSS': [50, 350, 1050, 1240],
                'IB': [70, 260, 800, 1190]}

intersections_2 = {'PM-IVT': [22, 190, 760, 1090],
                   'PM-ITSS': [17, 190, 500, 1110],
                   'PM-IB': [20, 150, 410, 1070],
                   'IVT-ITSS': [19, 190, 750, 1050],
                   'IVT-IB': [22, 140, 460, 1040],
                   'ITSS-IB': [17, 120, 500, 1090]}

intersections_3 = {'PM-IVT-ITSS': [5, 70, 500, 1020],
                   'PM-IVT-IB': [5, 70, 260, 1020],
                   'IVT-ITSS-IB': [5, 70, 300, 1000],
                   'PM-ITSS-IB': [5, 70, 250, 1040]}

intersections_4 = [3, 50, 200, 1000]

remove_percent = 0.07

# =====================================
# Генерация списков для первого дня
# =====================================
students_list = []
id_counter = 0

# Все 4 направления==============================================================
required_amount = intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [0, 1, 2, 3]))
id_counter = students_list[-1].id + 1

# 3 направления==================================================================
required_amount = intersections_3['PM-IVT-IB'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [0, 1, 3]))
id_counter = students_list[-1].id + 1

required_amount = intersections_3['PM-ITSS-IB'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [0, 2, 3]))
id_counter = students_list[-1].id + 1

required_amount = intersections_3['PM-IVT-ITSS'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [0, 1, 2]))
id_counter = students_list[-1].id + 1

required_amount = intersections_3['IVT-ITSS-IB'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [1, 2, 3]))
id_counter = students_list[-1].id + 1

# 2 направления================================================================================
required_amount = intersections_2['PM-IVT'][0] - intersections_3['PM-IVT-IB'][0] -\
    intersections_3['PM-IVT-ITSS'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [0, 1]))
id_counter = students_list[-1].id + 1

required_amount = intersections_2['PM-ITSS'][0] - intersections_3['PM-ITSS-IB'][0] -\
    intersections_3['PM-IVT-ITSS'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [0, 2]))
id_counter = students_list[-1].id + 1

required_amount = intersections_2['PM-IB'][0] - intersections_3['PM-IVT-IB'][0] -\
    intersections_3['PM-ITSS-IB'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [0, 3]))
id_counter = students_list[-1].id + 1

required_amount = intersections_2['IVT-IB'][0] - intersections_3['PM-IVT-IB'][0] -\
    intersections_3['IVT-ITSS-IB'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [1, 3]))
id_counter = students_list[-1].id + 1

required_amount = intersections_2['IVT-ITSS'][0] - intersections_3['IVT-ITSS-IB'][0] -\
    intersections_3['PM-IVT-ITSS'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [0, 1]))
id_counter = students_list[-1].id + 1

required_amount = intersections_2['ITSS-IB'][0] - intersections_3['PM-ITSS-IB'][0] -\
    intersections_3['IVT-ITSS-IB'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [0, 1]))
id_counter = students_list[-1].id + 1

# 1 направление================================================================================
required_amount = total_amount['PM'][0] - intersections_2['PM-ITSS'][0] - intersections_2['PM-IVT'][0] -\
    intersections_2['PM-IB'][0] - intersections_3['PM-ITSS-IB'][0] - intersections_3['PM-IVT-IB'][0] -\
    intersections_3['PM-IVT-ITSS'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [0]))
id_counter = students_list[-1].id + 1

required_amount = total_amount['IB'][0] - intersections_2['PM-IB'][0] - intersections_2['ITSS-IB'][0] -\
    intersections_2['IVT-IB'][0] - intersections_3['PM-ITSS-IB'][0] - intersections_3['PM-IVT-IB'][0] -\
    intersections_3['IVT-ITSS-IB'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [3]))
id_counter = students_list[-1].id + 1

required_amount = total_amount['ITSS'][0] - intersections_2['PM-ITSS'][0] - intersections_2['ITSS-IB'][0] -\
    intersections_2['IVT-ITSS'][0] - intersections_3['PM-ITSS-IB'][0] - intersections_3['IVT-ITSS-IB'][0] -\
    intersections_3['PM-IVT-ITSS'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [2]))
id_counter = students_list[-1].id + 1

required_amount = total_amount['IVT'][0] - intersections_2['IVT-ITSS'][0] - intersections_2['PM-IVT'][0] -\
    intersections_2['IVT-IB'][0] - intersections_3['IVT-ITSS-IB'][0] - intersections_3['PM-IVT-IB'][0] -\
    intersections_3['PM-IVT-ITSS'][0] - intersections_4[0]
for i in range(id_counter, id_counter+required_amount):
    students_list.append(Student(i, [1]))
id_counter = students_list[-1].id + 1

tables = [pd.DataFrame(columns=['ID', 'Наличие согласия', 'Приоритет', 'Балл Физика/ИКТ', "Балл Русский язык",
                           "Балл Математика", "Балл за индивидуальные достижения", "Сумма баллов"]) for _ in range(4)]

for i in range(len(students_list)):
    current_student_df = pd.DataFrame({'ID': [students_list[i].id], 'Наличие согласия': [students_list[i].agreement],
                                       'Приоритет': [0], 'Балл Физика/ИКТ': [students_list[i].scores[0]],
                                       "Балл Русский язык": [students_list[i].scores[1]],
                                       "Балл Математика": [students_list[i].scores[2]],
                                       "Балл за индивидуальные достижения": [students_list[i].scores[3]],
                                       "Сумма баллов": [sum(students_list[i].scores)]})
    for j in range(4):
        if j in students_list[i].priority:
            current_student_df.iat[0, 2] = students_list[i].priority.index(j) + 1
            tables[j] = pd.concat([tables[j], current_student_df])
# TODO Пофиксить общее количество поступивших

tables[0].to_excel('../tables/pm1.xlsx')
tables[1].to_excel('../tables/ivt1.xlsx')
tables[2].to_excel('../tables/itss1.xlsx')
tables[3].to_excel('../tables/ib1.xlsx')
