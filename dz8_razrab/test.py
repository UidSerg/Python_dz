from os import path
import shutil
import os

print('выберите директорию')
print(os.getcwd())
print(os.path.abspath('base.txt'))
papka = input('Введите имя папки куда копируем файл')
if os.path.isdir(os.path.join(os.getcwd(), papka)):
    shutil.copyfile('base.txt', os.path.join(os.getcwd(), papka))