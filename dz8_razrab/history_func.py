from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_records():

def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def search():
    """поиск слишком усложнил не исп, исп search_func"""
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
                
def change():
    object_search = input("введите данные для поиска:  ")                
    if object_search.isnumeric() == True:
            with open(file_base, "r", encoding="utf-8") as f:
                data = f.readlines()
                for i in range(len(data)):
                    if data[i].split()[-1] == object_search:
                        print(f'Ходите перезаписать контакт:\n {data[i]}')
                        otvet = input('Yes|No: ').lower()
                        if otvet == 'yes' or otvet == 'да':
                            fio =  input("введите фио:  ")
                            data[i] = str(f'{data[i].split()[0]} {fio} {object_search}\n')
                        else:
                            data[i] = data[i] 
            with open(file_base, 'w', encoding='utf-8') as f:
                f.writelines(data)
                print(f'Запись Изменена {data}')  