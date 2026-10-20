# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxlen = 0

        def max_diam(root):
            nonlocal maxlen
            if root is None:
                return 0
            
            left = max_diam(root.left)
            right = max_diam(root.right)

            maxlen = max(maxlen, left + right)

            return 1 + max(left, right)
        
        max_diam(root)
        return maxlen