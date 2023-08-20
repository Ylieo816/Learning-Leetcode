# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS - Recursion
class Solution:
    def put_data(self, root, depth, data):
        if root == None:
            return data    
        if len(data) < depth+1:
            data.append([])
        data[depth].append(root.val)
        self.put_data(root.left, depth+1, data)
        self.put_data(root.right, depth+1, data)
    
    
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        data = []
        self.put_data(root, 0, data)
        return data
    
# BFS - Loop
#         data = []
#         if root == None:
#             return data
        
#         q = [root]
#         while len(q) != 0:
#             data.append([node.val for node in q])
#             next_node = []
#             for node in q:
#                 if node.left != None:
#                     next_node.append(node.left)
#                 if node.right != None:
#                     next_node.append(node.right)
#             q = next_node
#         return data
        