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
            to_process = len(queue)
            curr = []

            for i in range(to_process):
                node = queue.popleft()
                if node:
                    curr.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if curr:
                res.append(curr)
        
        return res