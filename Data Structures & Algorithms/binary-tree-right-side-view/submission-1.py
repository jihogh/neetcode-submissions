# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            qLen = len(queue)

            for i in range(qLen):
                node = queue.pop()
                if node:
                    if i == qLen - 1:
                        res.append(node.val)
                    if node.left:
                        queue.appendleft(node.left)
                    if node.right:
                        queue.appendleft(node.right)
        
        return res