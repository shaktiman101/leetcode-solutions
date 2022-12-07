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
            #print(root.val)
            if (root.val >= low) and (root.val <= high):
                nonlocal ans
                #print(ans)
                ans += root.val
                
            solve(root.left)
            solve(root.right)
        solve(root)
        return ans