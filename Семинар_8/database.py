def write_name(name):   
    with open("telephone.txt","a", encoding="UTF-8") as file:
        file.write(name)

def search_name(name):
    with open("telephone.txt", "r", encoding="UTF-8") as file:
        a = file.readlines()
        for line in a:
            if name in line: 
                print(line)