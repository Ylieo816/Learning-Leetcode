# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

# Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
# Complexity Analysis
# Time Complexity: O(min(N1,N2)), where N1,N2 are the lengths of root1 and root2
# Space Complexity: O(min(H1,H2)), where H1,H are the heights of the trees of root1 and root2
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is root2: # is: determine whether the "memory addresses" between two variables are the same.
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))