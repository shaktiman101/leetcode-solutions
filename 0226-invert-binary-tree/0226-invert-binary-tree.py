# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def func(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            func(root.left)
            func(root.right)
        
        func(root)
        return root