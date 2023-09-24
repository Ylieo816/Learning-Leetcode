# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS recurision to traver from right to left
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def DFS(root, level):
            if root:
                if len(answer) == level:
                    answer.append(root.val)
                DFS(root.right, level + 1)
                DFS(root.left, level + 1)
            return
        answer = []
        DFS(root, 0)
        return answer

# BFS recurision (faster)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que = deque()
        if not root:    return []

        if not root.left and not root.right:    return [root.val]

        answer = []
        que.append(root)
        while que:
            next_que = deque()
            pre = -1
            while que:
                cur = que.popleft()

                if cur.left:
                    next_que.append(cur.left)

                if cur.right:
                    next_que.append(cur.right)
                pre = cur
            answer.append(pre.val)
            que = next_que
        return answer