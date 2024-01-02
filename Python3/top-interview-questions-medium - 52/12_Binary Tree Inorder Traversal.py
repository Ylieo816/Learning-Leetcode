# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def preorder(root):
#   return [root.val] + preorder(root.left) + preorder(root.right) if root else []

# def inorder(root):
#   return  inorder(root.left) + [root.val] + inorder(root.right) if root else []

# def postorder(root):
#   return  postorder(root.left) + postorder(root.right) + [root.val] if root else []

# Recurison
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            answer.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return answer

# Loop
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        stack = []
        while root or stack:
            while(root):
                stack.append(root)
                root = root.left
            root = stack.pop()
            answer.append(root.val)
            root = root.right
        return answer