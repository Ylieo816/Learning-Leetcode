# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity : O(n)
# Space complexity : O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = head, None
        while(pre):
            pre, cur, cur.next = pre.next , pre, cur
        return cur