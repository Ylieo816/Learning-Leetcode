# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Add all values to list, sort, and generate to list
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        value = []
        for lst in lists:
            # v = lst
            while lst:
                value += [lst.val]
                lst = lst.next
        value = sorted(value, reverse = True)
        answer = None
        for v in value:
            answer = ListNode(v, answer)

        return answer

# Divide and Conquer 
# Time complexity: O(N log k), where N is the total number of nodes, and k is the number of linked lists in the input vector
# Space complexity: O(log k), the depth of the tree is log k
class Solution:
    def merge(self, left, right):
        head = ListNode(-1)
        ptr = head
        while left and right:
            if left.val < right.val:
                ptr.next = left
                ptr = ptr.next
                left = left.next
            else:
                ptr.next = right
                ptr = ptr.next
                right = right.next
        while left:
            ptr.next = left
            ptr = ptr.next
            left = left.next
        while right:
            ptr.next = right
            ptr = ptr.next
            right = right.next
        return head.next

    def mergeSort(self, lists, start, end):
        if start == end:
            return lists[start]
        mid = start + (end - start) // 2
        left = self.mergeSort(lists, start, mid)
        right = self.mergeSort(lists, mid + 1, end)
        return self.merge(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.mergeSort(lists, 0, len(lists) - 1)