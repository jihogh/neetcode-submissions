# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lower, upper):
            curr_valid = False
            if root is None:
                return True
            
            if lower < root.val < upper:
                curr_valid = True

            left_valid = dfs(root.left, lower, min(root.val, upper))
            right_valid = dfs(root.right, max(lower, root.val), upper)

            if curr_valid and left_valid and right_valid:
                return True
            else:
                return False
        
        return dfs(root, float("-inf"), float("inf"))