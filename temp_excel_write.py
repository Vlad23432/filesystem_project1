import openpyxl


wb = openpyxl.Workbook()
sheet = wb.create_sheet('New table sheet')
active_sheet = wb['Sheet']
active_sheet.title = 'Renamed'  # смена имени листа таблицы
wb.remove(wb['Renamed'])  # удаление листа таблицы (передается именно лист)
wb.save('data/example.xlsx')

