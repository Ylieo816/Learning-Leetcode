# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS for Inorder traversal with early stopping
# time complexities: O(h)
# space complexities: O(k)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer = []

        def DFS(node):
            if not node:    return
            DFS(node.left)
            if len(answer) == k:
                return
            answer.append(node.val)
            DFS(node.right)

        DFS(root)
        return answer[-1]

# Loop for Inorder traversal
# Time complexity: O(log n) in avg case, O(n) in the worst case
# Space complexity: O(h)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            if not stack:   break

            node = stack.pop()
            k -= 1

            if k == 0:
                return node.val
            
            cur = node.right