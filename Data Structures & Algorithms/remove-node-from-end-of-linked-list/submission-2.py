# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        counter = 0

        while pointer:
            pointer = pointer.next
            counter += 1

        index = counter - n

        counter2 = 0
        pointer2 = head
        if index == 0:
            return head.next
            
        while counter2 != index - 1:
            pointer2 = pointer2.next
            counter2 += 1

        pointer2.next = pointer2.next.next

        return head