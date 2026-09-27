# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        number1 = ""
        number2 = ""

        while curr:
            number1 = str(curr.val) + number1
            curr = curr.next
        
        curr = l2
        while curr:
            number2 = str(curr.val) + number2
            curr = curr.next
        
        sum = str(int(number1) + int(number2))

        end = ListNode()
        curr = end
        prev = None

        for char in sum:
            curr.val = char
            curr.next = prev
            prev = curr
            curr = ListNode()
            print(char)

        return prev

