# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre = None
        p1 = p2 = head
        for i in range(n):
            p1 = p1.next
        while(p1):
            pre = p2
            p1 = p1.next
            p2 = p2.next
        
        if pre == None:
            head = head.next
        else:
            pre.next = p2.next
        return head
        
        # first answer
#         root = ListNode(0)
#         root.next = head
#         pointer1 = pointer2 = root
#         for i in range(n):
#             pointer1 = pointer1.next
        
#         while(pointer1.next):
#             pointer1 = pointer1.next
#             pointer2 = pointer2.next
        
#         pointer2.next = pointer2.next.next
        # return root.next