import pandas as pd
import openpyxl as opx

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


