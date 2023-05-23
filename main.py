from os import path

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
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")

def add_contact():
    last_name = input("Введите Фамилию:")
    name = input("Введите Имя:")
    father_name = input("Введите Отчество:")
    phone = int(input("Телефон:"))
    with open(file_base, "a", encoding="utf-8") as f:
        if name and phone:
            f.write(f'{last_id+1} {name} {last_name} {father_name} {phone}\n')

def search():
    object_search = input("введите данные для поиска:  ")
    if object_search.isnumeric() == True:
        print('это тел')
        with open(file_base, "r", encoding="utf-8") as f:
            sum = 0
            for line in f:
                if(line.split()[-1]) == object_search:
                    print(line)
                    sum = sum + 1
            if sum == 0:
                print(f'Телефон:{object_search} не найден')
        f.close()
    else:
        with open(file_base, "r", encoding="utf-8") as f:
            sum = 0
            for line in f:
                search_fio = line.split()
                result = map(str, search_fio) 
                result = list(filter(lambda x: x == object_search, result))
                if result:
                    print(line)
                    sum = sum +1
            if sum == 0:
                print('Не найдено!')
        f.close()        

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
                search()
            case "4":
                pass
            case "5":
                play = False
            case "6":
                pass
            case "7":
                pass
            case _:
                print("Try again!\n")

main_menu()