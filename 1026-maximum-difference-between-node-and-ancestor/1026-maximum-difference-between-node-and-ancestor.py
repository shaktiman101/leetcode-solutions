# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def func(root):
            if not root:
                return float('inf'), float('-inf')
            left_min, left_max = func(root.left)
            right_min, right_max = func(root.right)
            nonlocal ans
            min_ = min(left_min, right_min)
            max_ = max(left_max, right_max)
            if min_ != float('inf'):
                ans = max(ans, (root.val-min_))
            if max_ != float('-inf'):
                ans = max(ans, abs(root.val-max_))
            
            return min(left_min, right_min, root.val), max(left_max, right_max, root.val)
                       
        func(root)
        return ans
        