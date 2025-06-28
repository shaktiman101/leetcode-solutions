# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0

        def func(root):
            nonlocal max_dia
            if not root:
                return 0

            left_dia = func(root.left)
            right_dia = func(root.right)
            max_dia = max(max_dia, left_dia+right_dia)
            return 1+max(left_dia, right_dia)

        func(root)
        return max_dia