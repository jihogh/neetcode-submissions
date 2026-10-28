# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # use dfs to return height, but calculate diameter using the child calls before returning the height
        max_diam = 0

        def dfs(node):
            nonlocal max_diam

            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            max_diam = max(max_diam, left+right)

            return 1 + max(left, right)

        dfs(root)
        return max_diam