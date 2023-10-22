# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# space complexity: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd = head
        evenHead = even = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        odd.next = evenHead

        return head