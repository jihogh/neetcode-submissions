# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root, p, q):
            if root is None:
                return None
            
            if root.val == p.val:
                return p
            elif root.val == q.val:
                return q
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            if left and right:
                return root
            else:
                return left or right
        
        return dfs(root, p, q)
