from table_tools.check_tables import TableManager

tm = TableManager()
for day in range(1, 5):
    print(f"\n=== День {day} ===")
    tm.load_day(day)
    cutoff = tm.calculate_cutoff()
    stats = tm.get_statistics()
    print("Проходной балл:", cutoff)
    print("Статистика:", stats)