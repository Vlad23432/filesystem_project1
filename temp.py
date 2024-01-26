import os
import random as ran
import requests as req

base_dir = os.getcwd()  # get current working directory
print(os.listdir(base_dir))  # listdir(path) - список файлов и каталогов внутри папки из path
path_to_file = os.path.join(base_dir, 'data', 'pi_digits.txt')
with open(path_to_file, 'r') as f:
    data = f.read()

questions_path = os.path.join(base_dir, 'data', 'questions.txt')
with open(questions_path, 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        q1 = ran.choice(lines)
        q2 = ran.choice(lines)
        try:
            os.mkdir(os.path.join(base_dir, 'questions'))  # создать папку
        except:
            pass
        with open(os.path.join(base_dir, 'questions', f'bilet_{i}.txt'), 'w') as bilet:
            bilet.write(q1 + '\n' + q2)

bileti = os.path.join(base_dir, 'questions')


def remove_directory(dir_path):
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):  # если элемент является файлом
            os.remove(file_path)  # удалить файл
        else:  # если элемент - это папка
            remove_directory(file_path)  # рекурсивный вызов функции
    os.rmdir(dir_path)  # удалить папку


p = input('Insert directory: ')
remove_directory(p)


