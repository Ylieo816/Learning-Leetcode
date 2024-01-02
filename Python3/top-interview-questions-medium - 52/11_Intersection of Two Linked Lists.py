# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:
# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.

# Custom Judge:

# The inputs to the judge are given as follows (your program is not given these inputs):

# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Two Pointers
# Time - O(n+m)
# Space - O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one = headA
        two = headB

        # when shorter list reach our end, then run longer list
        # when running longer list, another reach out end and run shorter one
        # second round will fund the interaction
        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one

# Hashset
# Time Complexity - O(n+m)
# Space Complexity - O(n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first_set=set()
        curr=headA
        
        while curr:
            first_set.add(curr)
            curr=curr.next
        
        curr = headB
        while curr:
            if curr in first_set:
                return curr
            curr=curr.next

        return None

# Stack
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA, stackB = ['A'], ['B']

        while headA or headB:
            if headA:
                stackA.append(headA)
                headA = headA.next
            
            if headB:
                stackB.append(headB)
                headB = headB.next

        preNode = None
        while stackA and stackB:
            nodeA = stackA.pop(-1)
            nodeB = stackB.pop(-1)

            if nodeA != nodeB:
                return preNode

            preNode = nodeA