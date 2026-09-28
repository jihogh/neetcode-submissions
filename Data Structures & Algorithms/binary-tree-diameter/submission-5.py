# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxim = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getMaxHeight(root):
            if root is None:
                return 0

            return 1 + max(getMaxHeight(root.left), getMaxHeight(root.right))
        
        if root is None:
            return 0

        leftH = getMaxHeight(root.left)
        rightH = getMaxHeight(root.right)
        diam = leftH + rightH

        self.maxim = max(diam, self.maxim)

        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
    
        return self.maxim