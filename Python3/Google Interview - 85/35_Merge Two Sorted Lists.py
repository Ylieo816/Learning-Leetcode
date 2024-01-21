# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Complexity Analysis
# Time complexity : O(n+m)
# Space complexity : O(1)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = ptr = ListNode(0)
        while(l1 and l2):
            if l1.val < l2.val:
                new_list.next = l1
                l1 = l1.next
            else:
                new_list.next = l2
                l2 = l2.next
            new_list = new_list.next
        new_list.next = (l1 or l2)
        return ptr.next