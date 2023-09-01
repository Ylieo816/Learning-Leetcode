# Given a binary tree, determine if it is height-balanced.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #  Balanced Binary Tree: Left & Right is balanced and diff is less than 1
        return (self.getHight(root) >= 0)

    def getHight(self, root: Optional[TreeNode]):
        # if no root, False
        if not root:
            return 0
        # get Left and Right hight
        left_subTree, right_subTree = self.getHight(root.left), self.getHight(root.right)
        # if only one subTree < 0 , False
        # if two subTree diff is more than 1, False
        if left_subTree < 0 or right_subTree < 0 or abs(left_subTree - right_subTree) > 1:
            return -1
        return max(left_subTree, right_subTree) + 1