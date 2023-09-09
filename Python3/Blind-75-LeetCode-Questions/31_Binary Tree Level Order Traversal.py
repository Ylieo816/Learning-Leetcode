# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS - Recursion
class Solution:
    def put_data(self, node, level, data):
        if not node:
            return data
        if len(data) < level +1:
            data.append([])
        data[level].append(node.val)
        self.put_data(node.left, level+1, data)
        self.put_data(node.right, level+1, data)
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        data = []
        self.put_data(root, 0, data)
        return data

# BFS - Loop
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        data = []
        if not root: return data
        
        q = [root]
        while(len(q) != 0):
            data.append([n.val for n in q])
            next_node = []
            for node in q:
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            q = next_node
        return data