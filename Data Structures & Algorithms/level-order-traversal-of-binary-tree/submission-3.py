# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque()
        queue.append(root)

        while queue:
            level = []
            numL = len(queue)

            for i in range(numL):
                node = queue.pop()
                if node:
                    level.append(node.val)
                    queue.appendleft(node.left)
                    queue.appendleft(node.right)
            
            if level:
                res.append(level)
        
        return res