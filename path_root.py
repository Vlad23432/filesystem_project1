from pathlib import Path
from os import path


class MyPath:
    """
    Класс для работы с путями в проекте.
    Args:
        path_str: Путь к файлу или папке на компьютере
    Attributes:
        path: Объект pathlib, представляет путь
        is_file: True, если объект является файлом. False - если директорией
        is_dir: True, если объект является директорией. False - если файлом
    """
    def __init__(self, path_str):
        self.path = Path(path_str)
        self.is_file = self.path.is_file()
        self.is_dir = self.path.is_dir()

    def read_file(self):
        """
        Чтение текста из файла
        :return: Строка текста из файла
        """
        if not self.is_file:  # если параметр is_file = False
            raise ValueError("Невозможно прочитать текст. Передан не текстовый файл.")
        with open(self.path, 'rb') as file:
            return file.read()




