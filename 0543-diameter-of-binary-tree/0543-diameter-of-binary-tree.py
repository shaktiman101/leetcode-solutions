# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def func(root):
            if not root:
                return 0
            nonlocal ans
            l = func(root.left)
            r = func(root.right)
            ans = max(ans, l+r)
            return 1+max(l, r)
        func(root)
        return ans
    
    
    
        
        
        
        
        
        
        
        
        
        res = 0
        def func(root):
            nonlocal res
            if not root:
                return 0
            l = func(root.left)
            r = func(root.right)
            res = max(res, l+r)
            print(1+max(l, r))
            return 1+max(l,r)
        
        func(root)
        return res
            
            
        