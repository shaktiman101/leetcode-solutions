# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                yield root.val
                return
            yield from dfs(root.left)
            yield from dfs(root.right)
        return list(dfs(root1)) == list(dfs(root2))
        
        leaves = []
        def traverse(root):
            if not root:
                return
            if (not root.left) and (not root.right):
                nonlocal leaves
                leaves.append(root.val)
                return
            traverse(root.left)
            traverse(root.right)
        traverse(root1)
        leaves = leaves[::-1]
        print(leaves)
        
        def traverse2(root):
            if not root:
                return True
            if (not root.left) and (not root.right):
                nonlocal leaves
                if leaves and root.val == leaves[-1]:
                    leaves.pop()
                    return True
                return False
            return traverse2(root.left) and traverse2(root.right)
            
        res = traverse2(root2)
        if not leaves and res:
            return True
        return False