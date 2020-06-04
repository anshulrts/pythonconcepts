import understandingimport

def importingmodules():
    understandingimport.start()

switcher = {
    1: importingmodules
}

def start():
    while(True):
        print("       Menu")
        print(" 1. Importing Modules")

        ch = input("Enter choice : ")
        callmethod = switcher.get(int(ch), lambda: print('Invalid'))
        callmethod()

if __name__ == "__main__":
    start()