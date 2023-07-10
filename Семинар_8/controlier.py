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
                d = input_delit()

            case 4:
                rename = input_rename()

            case 4:
                name = input_name()
                write_name(name)
                print("Успешно отсортированно \n")  
            case 6:
                print("Выход")
                return()

main()