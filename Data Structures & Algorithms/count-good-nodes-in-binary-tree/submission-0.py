# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_curr):
            if root is None:
                return 0 
            if root.val >= max_curr:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            
            return dfs(root.left, max_curr) + dfs(root.right, max_curr)
    
        return dfs(root, root.val)
            

                

            








        