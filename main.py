import understanding_import
import global_local_variable

def importing_modules():
    understanding_import.start()

def global_local():
    global_local_variable.start()

switcher = {
    1: importing_modules,
    2: global_local
}

def start():
    while(True):
        print("       Menu")
        print(" 1. Importing Modules")
        print(" 2. Global vs Local Variable")

        ch = input("Enter choice : ")
        call_method = switcher.get(int(ch), lambda: print('Invalid'))
        call_method()

if __name__ == "__main__":
    start()