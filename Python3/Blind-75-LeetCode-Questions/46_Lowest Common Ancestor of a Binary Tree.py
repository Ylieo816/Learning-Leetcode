# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Complexity
# - Time complexity: O(n), where n is number of nodes, since each node at most visited once

# - Space complexity: O(h), where h is the height of the tree, since in worst case (e.g. completely skewed tree) each node along the height is visited once. Space complexity determined by height of recursion tree which is at most O(h)O(h)O(h)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # check if root == p or q, it means root sub includes p or q
        if not root or root == p or root == q:
            return root

        # check if root sub include p or q under left or right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if root includes left and right, means it is the lowest common ancestor
        # if not, return which left or right is not empty
        return (root if left and right else (left or right))        