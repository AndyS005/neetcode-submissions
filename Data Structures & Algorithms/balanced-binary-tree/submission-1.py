# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        def dfs(root):
            if root == None:
                return 0

            left, right = dfs(root.left), dfs(root.right)
            if left - 1 > right or right - 1 > left:
                self.flag = False

            return 1 + max(left, right)
        dfs(root)
        return self.flag
