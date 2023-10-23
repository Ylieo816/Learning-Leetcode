# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Complexity
# Time complexity: O(N)
# Space complexity: O(W) width of the tree
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if not root:
            return answer

        q = deque()
        q.append(([root, 0]))

        while q:
            node, level = q.popleft()
            if level >= len(answer):
                answer.append([])

            if level % 2 == 0:
                answer[level].append(node.val)
            else:
                answer[level].insert(0, node.val)
            
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return answer