from database import*
from view import*

def main():
    while True:
        num = input_num()
        match num:
            case 1:
                name = input_name()
                write_name(name)
                print("Успешно записано \n")
            case 2:
                s = input_search()
                search_name(s)
                print("Успешно найдено \n")
            case 3:
                name = input_name()
                write_name(name)
                print("Успешно удалено \n")
            case 4:
                name = input_name()
                write_name(name)
                print("Успешно найдено \n")
            case 5:
                name = input_name()
                write_name(name)
                print("Успешно переместил \n")
            case 6:
                print("Выход")
                return()

main()