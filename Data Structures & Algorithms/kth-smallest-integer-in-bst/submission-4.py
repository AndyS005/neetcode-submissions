# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0 
        self.res = 0 

        def dfs(root):
            if root == None:
                return
            
            left = dfs(root.left)
            self.count +=1
            if self.count == k:
                self.res = root.val
                return
            right = dfs(root.right)

            return left or right
        dfs(root)
        return self.res











        