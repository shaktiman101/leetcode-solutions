# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if not root:
                return 0

            l = height(root.left)
            if isinstance(l, bool):
                return l
            
            r = height(root.right)
            if isinstance(r, bool):
                return r

            if abs(l-r) > 1:
                return False
            return 1+max(l, r)

        ans = height(root)
        if isinstance(ans, bool):
            return ans

        return True