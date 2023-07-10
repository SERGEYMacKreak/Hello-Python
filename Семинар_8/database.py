from view import*

def write_name(name):   
    with open("telephone.txt","a", encoding="UTF-8") as file:
        file.write(name)

def search_name(s):
    with open("telephone.txt", "r", encoding="UTF-8") as file:
        a = file.readlines()
        for line in a:
            if s in line: 
                print(line)
              

def input_delit():
  print("\n    id |    ФИО      | Дата рождения")
  with open("telephone.txt", "r", encoding="UTF-8") as file: #выводим базу + придаем номера строкам
    dels = file.readlines()
    coint = 1
    for line in dels:
      print(f"№{coint} {line}")
      coint += 1
  index_delete = int(input("Введите номер строки для удаления: "))-1 #выбираем какую строку удалить (-1 так как индекс идет с 0)
  telephone_lines = dels
  del_lines = telephone_lines[index_delete]
  telephone_lines.pop(index_delete)
  print(f"Удалена запись: {del_lines}\n")

  with open("telephone.txt", "w", encoding="utf-8") as data: #формируем новую базу без удал. элимента
    data.write("\n".join(telephone_lines))


def input_rename():
  print("\n    id |    ФИО      | Дата рождения")
  with open("telephone.txt", "r", encoding="UTF-8") as file: #выводим базу + придаем номера строкам
    rename = file.readlines()
    coint = 1
    for line in rename:
      print(f"№{coint} {line}")
      coint += 1
  index_rename = int(input("Введите номер строки который нужно изменить: "))-1 #выбираем какую строку изменить (-1 так как индекс идет с 0)
  telephone_lines = rename
  rename_line = telephone_lines[index_rename]
  new_line = input_name() #вызываем функцию ввода новых данных
  telephone_lines[index_rename] = new_line
  print()
  print(f"Запись — {rename_line} изменена на — {new_line}\n")

  with open("telephone.txt", "w", encoding="utf-8") as data: #формируем новую базу с изменныным элементом
    data.write("".join(telephone_lines))

# def sort():
#     with open("telephone.txt", "r", encoding="UTF-8") as file:
#         a = file.readlines()
#         a.sort(key = lambda x: int(x.split(",")[2]))
#         print(a)