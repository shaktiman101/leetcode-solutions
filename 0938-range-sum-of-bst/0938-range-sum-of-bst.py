# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        ans = 0
        def solve(root):
            if not root:
                return
            if root.val >= low and root.val <= high:
                nonlocal ans
                ans += root.val
            if root.val >= low:
                solve(root.left)
            if root.val <= high:
                solve(root.right)
        solve(root)
        return ans