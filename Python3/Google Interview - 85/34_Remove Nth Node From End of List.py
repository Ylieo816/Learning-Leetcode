# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Complexity Analysis
# Time complexity : O(L), the list of L nodes
# Space complexity : O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:   return

        ptr1, ptr2 = head, head

        for i in range(n):
            ptr1 = ptr1.next

        if not ptr1:    
            return ptr2.next

        while ptr1.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        ptr2.next = ptr2.next.next
        return head