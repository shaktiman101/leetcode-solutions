# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = deque([root])
        
        count = 0
        while stack:
            node = stack.popleft()
            count += 1
            if node.left:
                stack.append(node.left)
            else:
                count += len(stack)
                break
            if node.right:
                stack.append(node.right)
            else:
                count += len(stack)
                break
        return count
            
        