# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        left, right = self.isSubtree(root.left, subRoot), self.isSubtree(root.right, subRoot)
        return self.isSameTree(root, subRoot) or left or right

    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)