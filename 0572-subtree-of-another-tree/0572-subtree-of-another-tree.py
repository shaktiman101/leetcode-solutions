# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if not subRoot:
    #         return True
    #     if not root:
    #         return False

    #     if self.check(root, subRoot):
    #         return True

    #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    # def check(self, root, subRoot):
    #     if not root and not subRoot:
    #         return True
        
    #     if (root and not subRoot) or (not root and subRoot):
    #         return False

    #     if root.val == subRoot.val: 
    #         left_subtree = self.check(root.left, subRoot.left)
    #         right_subtree = self.check(root.right, subRoot.right)
    #         return left_subtree and right_subtree
        
    #     return False
        
        # def check(root1, root2):
        #     if root1 is None and root2 is None:
        #         return True
        #     if root1 is None or root2 is None:
        #         return False
            
        #     if root1.val == root2.val:
        #         res1 = check(root1.left, root2.left)
        #         res2 = check(root1.right, root2.right)
        #         return res1 and res2

        #     return False

        # if root is None:
        #     return False

        # if check(root, subRoot):
        #     return True
            
            
        # return self.isSubtree(root.right, subRoot) or self.isSubtree(root.right, subRoot)
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
            