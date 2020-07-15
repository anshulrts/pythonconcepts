import understanding_import
import global_local_package.global_local_variable
import linked_list

def importing_modules():
    understanding_import.start()

def global_local():
    global_local_package.global_local_variable.start()

def linked_list():
    linked_list.start()

switcher = {
    1: importing_modules,
    2: global_local,
    3: linked_list
}

def start():
    while(True):
        print("       Menu")
        print(" 1. Importing Modules")
        print(" 2. Global vs Local Variable")
        print(" 3. Linked List")

        ch = input("Enter choice : ")
        call_method = switcher.get(int(ch), lambda: print('Invalid'))
        call_method()

if __name__ == "__main__":
    start()