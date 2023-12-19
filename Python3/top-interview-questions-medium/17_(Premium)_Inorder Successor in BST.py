# Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

# The successor of a node p is the node with the smallest key greater than p.val.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Successor for BST
# Recursion
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return left if left != None else root

# Loop 
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor


# Predecessor for BST
# class Solution:
#     def inorderPredecessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
#         if not root:
#             return None

#         if root.val >= p.val:
#             return self.inorderPredecessor(root.left, p)
#         else:
#             right = self.inorderPredecessor(root.right, p)
#             return right if right != None else root