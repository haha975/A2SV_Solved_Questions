# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.sum_val=0
        
        def rec(root):
            if root and  root.val%2==0:
                if root.left and  root.left.left:
                    self.sum_val+=root.left.left.val
                if root.left and root.left.right:
                    self.sum_val+=root.left.right.val
                if root.right and root.right.left:
                    self.sum_val+=root.right.left.val
                if root.right and root.right.right:
                    self.sum_val+=root.right.right.val
                rec(root.left)
                rec(root.right)
            else:
                if root and  root.left:
                    rec(root.left)
                if root and root.right:
                    rec(root.right)
        rec(root)
        return self.sum_val


        