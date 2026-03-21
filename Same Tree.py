# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans=[]
        def help(p, q):
            if not p and not q:
                return
            if not p or not q:
                ans.append(False)
                return
            
            ans.append(p.val == q.val)
            help(p.left, q.left)
            help(p.right, q.right)
        help(p,q)
        if False in ans:
            return False
        else:
            return True



        
