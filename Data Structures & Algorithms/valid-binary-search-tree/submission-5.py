# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lower, upper):
            if root is None:
                return True
            
            if lower < root.val < upper:
                return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)
            else:
                return False
        
        return dfs(root, float("-inf"), float("inf"))