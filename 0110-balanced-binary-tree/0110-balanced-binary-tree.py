# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def func(root):
            if not root:
                return 0
            lh = func(root.left)
            if isinstance(lh, bool):
                return False
            rh = func(root.right)
            if isinstance(rh, bool):
                return False
            if abs(lh-rh) > 1:
                return False
            return max(lh, rh)+1
        return func(root)
        
        
        
        
        
        
        
        
        
        
        
        
        def func(root):
            if not root:
                return 0
            height_left = 1+func(root.left)
            height_right = 1+func(root.right)
            if isinstance(height_left, int) and isinstance(height_left, int) and height_left != height_right:
                return False
            else:
                return height_left
        return func(root)
        