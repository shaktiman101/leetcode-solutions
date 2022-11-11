# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def func(root):
            if not root:
                return 0
            left_depth = 1 + func(root.left)
            right_depth = 1 + func(root.right)
            return max(left_depth, right_depth)
        
        return func(root)
        