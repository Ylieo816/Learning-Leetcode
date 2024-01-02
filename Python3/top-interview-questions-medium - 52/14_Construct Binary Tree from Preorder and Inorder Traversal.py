# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Complexity
# Time complexity:. O(n)
# Space complexity:. O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_table = {}
        for i in range(len(inorder)):
            inorder_table[inorder[i]] = i

        pre_idx = [0]
        def treePartition(start, end):
            if start > end:
                return None
            
            root_val = preorder[pre_idx[0]]
            pre_idx[0] += 1
            root = TreeNode(root_val)
            idx = inorder_table[root_val]
            root.left = treePartition(start, idx - 1)
            root.right = treePartition(idx + 1, end)
            return root

        return treePartition(0, len(inorder) - 1)

# Easy logic but too late
# check by inorder and preorder characteristic, divide to left and right sidt
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root