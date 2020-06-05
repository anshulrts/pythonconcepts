import understanding_import

def importing_modules():
    understanding_import.start()

switcher = {
    1: importing_modules
}

def start():
    while(True):
        print("       Menu")
        print(" 1. Importing Modules")

        ch = input("Enter choice : ")
        call_method = switcher.get(int(ch), lambda: print('Invalid'))
        call_method()

if __name__ == "__main__":
    start()