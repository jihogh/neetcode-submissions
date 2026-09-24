# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        new = ListNode(0, None)
        start = new

        while p1 and p2:
            if p1.val < p2.val:
                new.next = p1
                new = new.next
                p1 = p1.next
            else:
                new.next = p2
                new = new.next
                p2 = p2.next
        
        if p1:
            new.next = p1
        elif p2:
            new.next = p2
        
        return start.next