# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self,root: Optional[TreeNode], k: int) -> bool:
        lis=[]
        def helper(root):
            if root:
                lis.append(root.val)
                helper(root.left)
                helper(root.right)
                return 
        helper(root)
        lis.sort()
        left=0
        right=len(lis)-1
        while left<right:
            su=lis[left]+lis[right]
            if su<k:
                left+=1
            elif su>k:
                right-=1
            elif su==k:
                return True
        return False
