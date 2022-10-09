# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        # s = set()
        # def preorder(root):
        #     if not root:
        #         return False
            
        #     if k - root.val in s:
        #         return True
        #     s.add(root.val)
        #     return (preorder(root.left) or preorder(root.right))

        # return preorder(root)
        if not root:
            return False

        q = deque([root])
        visited = set()
        while q:
            node = q.popleft()
            if k - node.val in visited:
                return True
            visited.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
