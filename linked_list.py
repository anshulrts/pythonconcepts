class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, n):
        if self.head is None:
            self.head = n
            return

        n.next = self.head
        self.head = n

    def print_list(self):
        temp = self.head

        while (temp):
            print(temp.data, end="-> ")
            temp = temp.next


def start():

    # Create Linked List
    llist = LinkedList()

    #region Initialize
    # Initialize Linked List
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    #endregion

    llist.print_list()

    #region Insert At Beginning
    zero = Node(0)
    print()
    print("After Inserting Zero at beginning")
    llist.insert_at_beginning(zero)
    llist.print_list()
    #endregion

if __name__ == "__main__":
    start()