from os import path
import shutil
import os

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    """Вывод списка контактов"""
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")

def add_contact():
    """Добавляем контакт в конце списка"""
    last_name = input("Введите Фамилию:")
    name = input("Введите Имя:")
    father_name = input("Введите Отчество:")
    phone = int(input("Телефон:"))
    with open(file_base, "a", encoding="utf-8") as f:
        if last_name and name and father_name and phone:
            f.write(f'{last_id+1} {last_name} {name} {father_name} {phone}\n')
##____add_contact_____________END

def search_func(book: list, poisk: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    return list(filter(lambda contact: poisk.lower() in contact.lower(), book))

##____search_func_____________END

       
def change():
    """Изменение контакта"""
    object_search = input("введите данные для поиска:  ")
    result = search_func(all_data, object_search)
    count = len(result)
    if count == 0:
        print('Ничего не найдено по вашему запросу')
    elif count == 1:
        start = int(result[0].split()[0])
        if count > 1:
            for i in range(count):
                print(f'{i+1}.[{result[i]}]')
            new_search = int(input("Уточните какой контакт хотите изменить?: "))
            if new_search > 0 and count+1 > new_search:
                print(f'Изменяем [{result[new_search-1]}]')
                start = int(result[new_search-1].split()[0])
            else:
                print("Указано неверноe значение для редактирования") 
            
        last_name = input("Введите Фамилию:")
        name = input("Введите Имя:")
        father_name = input("Введите Отчество:")
        phone = int(input("Телефон:"))
        all_data[start-1] = str(f'{all_data[start-1].split()[0]} {last_name} {name} {father_name} {phone}')
        with open(file_base, 'w', encoding='utf-8') as f:
            for i in range(len(all_data)):
                with open(file_base, 'a', encoding='utf-8') as f:
                    f.write(f'{all_data[i]}\n') 
            print(f'Запись Изменена!')
##____change_____________END
 

def delete_contact():
    '''Удаление контакта''' 
    object_search = input("Введите что удаляем?: ")
    result = search_func(all_data, object_search)
    count = len(result)
    if count == 0:
        print('Ничего не найдено!')
    if count == 1:
        start = int(result[0].split()[0])
        del_func(start, all_data)
    else:
        for i in range(count):
            print(f'{i+1}.[{result[i]}]')
        new_search = int(input("Уточните какой контакт хотите удалить?: "))
        if new_search > 0 and count+1 > new_search:
            print(f'Удаляем [{result[new_search-1]}]')
            start = int(result[new_search-1].split()[0])
            del_func(start, all_data)
        else:
            print("Указано неверноe значение для удаления")
            
##____delete_contact_____________END         

def del_func(start: int, all_data: list):
    """удаление"""        
    with open(file_base, 'w', encoding='utf-8') as f:
        for i in range(start-1):
            with open(file_base, 'a', encoding='utf-8') as f:
                f.write(f'{all_data[i]}\n') 
    for i in range(start, len(all_data)):
        with open(file_base, 'a', encoding='utf-8') as f:
            numeric=int(all_data[i].split()[0])
            line= str(all_data[i])
            srez = line[len(str(numeric)):] 
            srez = str(numeric-1)+srez
            f.write(f'{srez}\n')
    print(f'Удалено!!!')  
##____del_func_____________END

def export():
    print('выберите директорию')
    print(os.getcwd())
    print(os.path.abspath('base.txt'))


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_contact()
            case "3":
                object_search = input("введите данные для поиска:  ")
                result = search_func(all_data, object_search)
                for i in range(len(result)):
                    print(result[i])
            case "4":
                play = False
                change()
            case "5":
                play = False
                delete_contact()
            case "6":
                export()
            case "7":
                pass
            case _:
                print("Try again!\n")

main_menu()