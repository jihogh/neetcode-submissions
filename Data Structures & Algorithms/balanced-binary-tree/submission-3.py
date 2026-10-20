# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return (0, True)
            
            leftH, Lbalanced = height(root.left)
            rightH, Hbalanced = height(root.right)

            if Lbalanced and Hbalanced and abs(leftH - rightH) <= 1:
                return (1 + max(leftH,rightH), True)
            
            return (1 + max(leftH,rightH), False)
        
        height, isBal = height(root)
        return isBal