# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, upper, lower):
            if root is None:
                return True
            
            if lower < root.val < upper:
                return True and dfs(root.left, root.val, lower) and dfs(root.right, upper, root.val)
            else:
                return False

        return dfs(root, float('inf'), float('-inf'))