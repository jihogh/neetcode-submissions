# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque([root])

        while queue:
            curlen = len(queue)
            level = []

            # pop exactly how many nodes there are before we add any nodes
            for _ in range(curlen):
                curnode = queue.popleft()

                if curnode:
                    level.append(curnode.val)

                    queue.append(curnode.left)
                    queue.append(curnode.right)

            if level:
                res.append(level)
        
        return res