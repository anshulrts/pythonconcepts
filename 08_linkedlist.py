class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def CreateLinkedList(self):
        head = ListNode(1)
        first = ListNode(2, head)
        second = ListNode(3, first)
        third = ListNode(4, second)
        return third


sol = Solution()
head = sol.CreateLinkedList()

temp = head

while(temp is not None):
    print(temp.value, end="->")
    temp = temp.next