# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        kth = None

        def dfs(root):
            nonlocal count
            nonlocal kth
            if root is None:
                return
            
            dfs(root.left)

            count += 1
            if count == k:
                kth = root.val
                return
            
            dfs(root.right)
        
        dfs(root)
        return kth