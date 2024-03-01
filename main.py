import excelWriter
import excelReader
import path_root


def menu():
	text = """
	Выберите действие с программой:
	1 - Прочитать файл
	2 - Записать в файл
	3 - Просмотреть содержимое папки
	4 - Создать папку 
	5 - Удалить файл/папку 
	6 - Переименовать файл/папку
	7 - Существует ли путь?
	8 - Получить размер 
	9 - Время последнего изменения 
	10 - Работа с файлами excel
	-------------------------------
	0 - завершить работу 
	"""
	print(text)
	choice = int(input())
	return choice


def excel_menu():
	text = """
	1 - Записать файл excel
	2 - Прочитать файл excel
	-------------------------------
	0 - завершить работу 
	"""
	print(text)
	choice = int(input())
	return choice


def excel_reader_menu():
	text = """
		1 - Вывести все листы таблицы
		2 - Получить значение ячейки
		3 - Вывести таблицу на экран 
		-------------------------------
		0 - завершить работу 
		"""
	print(text)
	choice = int(input())
	return choice


def excel_writer_menu():
	text = """
		1 - Записать данные в таблицу
		2 - Обновить значения в ячейке
		3 - Добавить формулу в таблицу
		4 - Сохранить таблицу
		5 - Преобразовать в CSV
		-------------------------------
		0 - завершить работу 
		"""
	print(text)
	choice = int(input())
	return choice


def excel_worker(path):
	choice = excel_menu()
	while choice != 0:
		match choice:
			case 1:
				w_menu = excel_writer_menu()
				table = excelWriter.ExcelWriter()
				while w_menu != 0:
					match w_menu:
						case 1:
							pass
						case 2:
							row = int(input('Строка: '))
							col = int(input('Столбец: '))
							val = int(input('Значение: '))
							table.update_value(row, col, val)
							print('Обновлено')
						case 3:
							pass
						case 4:
							pass
						case 5:
							pass
			case 2:
				r_menu = excel_reader_menu()
				table = excelReader.ExcelReader(str(path))
				while r_menu != 0:
					match r_menu:
						case 1:
							sheets = table.get_sheetnames()
							print(sheets)
						case 2:
							name = input('Имя листа: ')
							cell = input('Адрес ячейки (А1): ')
							value = table.get_cell_value(name, cell)
							print(value)
						case 3:
							name = input('Имя листа: ')
							table.iterate_excel_sheet(name)

					r_menu = excel_reader_menu()

		choice = excel_menu()


def main():
	choice = menu()
	while choice != 0:
		path = input('Введите путь: ')
		my_path = path_root.MyPath(path)

		match choice:
			case 1:
				content = my_path.read_file()
				print(content)
			case 2:
				text = input('Текст для файла:')
				my_path.write_file(text)
				print('Успешно записано!')
			case 3:
				try:
					my_path.list_dir()
				except ValueError as e:
					print(e)
			case 4:
				try:
					my_path.create_dir()
					print('Создано!')
				except ValueError as e:
					print(e)
			case 5:
				try:
					my_path.delete()
					print('Удалено!')
				except ValueError as e:
					print(e)
			case 6:
				new_name = input('Введите новое имя: ')
				try:
					my_path.rename(new_name)
					print('Готово!')
				except ValueError as e:
					print(e)
			case 7:
				if my_path.is_exists():
					print('Такой путь существует!')
				else:
					print('Пути не существует.')
			case 8:
				try:
					size = my_path.get_size()
					print(f'Размер файла {size} байт')
				except ValueError as e:
					print(e)
			case 9:
				print('Последнее изменение:', my_path.get_mtime())
			case 10:
				excel_worker(my_path)

		choice = menu()


main()
