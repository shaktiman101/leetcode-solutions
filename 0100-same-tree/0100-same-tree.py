# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def func(p, q):
            # if not p and not q:
            #     return True
            # if (not p and q) or (p and not q):
            #     return False
            if not p:
                return q==None
            if not q:
                return p==None
            if p.val != q.val:
                return False
            r1 = func(p.left, q.left)
            r2 = func(p.right, q.right)
            return r1 and r2
        
        return func(p, q)