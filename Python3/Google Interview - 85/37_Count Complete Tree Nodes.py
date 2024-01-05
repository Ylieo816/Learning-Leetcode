# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
# Complexity Analysis
# Time complexity : O(NlogN)
# Space complexity : O(1)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # find left side level
        def depthOfLeft(node):
            level = 0
            while node:
                level += 1
                node = node.left
            return level

        # find right side level
        def depthOfRight(node):
            level = 0
            while node:
                level += 1
                node = node.right
            return level

        leftLevel = depthOfLeft(root.left)
        rightLevel = depthOfRight(root.right)

        # if left and right same, it means there are completed BT, so return total node num
        if leftLevel == rightLevel:
            return 2 ** (leftLevel + 1) - 1
        # if right < left, going to sub level (right side) and plus 1 for previous level
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)