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
	-------------------------------
	0 - завершить работу 
	"""
	print(text)
	choice = int(input())
	return choice


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

		choice = menu()


main()
