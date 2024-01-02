# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS - Recursion
class Solution: 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def DFS(left, root, right):
            if not root:
                return True
            if not(left < root.val < right):
                return False
        
            return DFS(left, root.left, root.val) and DFS(root.val, root.right, right)
        return DFS(float("-inf"), root, float("inf"))



# DFS - Loop
class Solution:
    def check_list(self, lst):
        for i in range(len(lst) - 1):
            if lst[i+1] <= lst[i]:
                return False
        return True
            
    def put_value(self, root):
        stack, seq_data = [], []
        
        while(root or stack):
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                seq_data.append(root.val)
                root = root.right
        return seq_data
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return not root or self.check_list(self.put_value(root))