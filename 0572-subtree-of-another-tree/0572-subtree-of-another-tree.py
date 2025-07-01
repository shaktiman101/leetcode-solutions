# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # def func(root, subRoot):
        #     if not root and not subRoot:
        #         return True

        #     if (not root and subRoot) or (root and not subRoot):
        #         return False
            
        #     if root.val == subRoot.val:
        #         l = func(root.left, subRoot.left)
        #         r = func(root.right, subRoot.right)
        #         if l and r:
        #             return True
            
        #     return func(root.left, subRoot) or func(root.right, subRoot)

        # return func(root, subRoot)

        if not subRoot:
            return True
        if not root:
            return False

        if self.check(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def check(self, root, subRoot):
        if root and not subRoot:
            return False
        if not root and subRoot:
            return False
        if not root and not subRoot:
            return True

        if root.val == subRoot.val:
            if self.check(root.left, subRoot.left) and self.check(root.right, subRoot.right):
                return True
        return False