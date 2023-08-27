# The Python interpreter executes scripts starting at the top of the file,
# and there is no specific function that Python automatically executes like in other languages.

# Having a defined starting point for the execution of a program is useful for
# understanding how a program works. Python programmers have come up with several conventions
# to define this starting point.

# Article Link - https://realpython.com/python-main-function/

# Best way to create python files:

from time import sleep

print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Begin Processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def main():
    data = "My data read from the web"
    print(data)
    modified_data = process_data(data)
    print(modified_data)

if __name__ == '__main__':
    main()