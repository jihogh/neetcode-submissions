# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(root, maxSoFar):
            nonlocal good
            if root is None:
                return
            
            if root.val >= maxSoFar:
                good += 1
            
            dfs(root.left, max(maxSoFar, root.val))
            dfs(root.right, max(maxSoFar, root.val))
        
        dfs(root, root.val)

        return good