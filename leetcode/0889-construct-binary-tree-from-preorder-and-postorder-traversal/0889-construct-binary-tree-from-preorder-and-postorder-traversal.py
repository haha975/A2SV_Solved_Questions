# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos={v:i for i,v in enumerate(postorder)}
        def func(a,b,c,d):
            if a>b or c>d:
                return None
            root =TreeNode(preorder[a])
            if a==b:
                return root

            i=pos[preorder[a+1]]
            left=i-c+1
            root.left=func(a + 1, a + left, c, i)
            root.right=func(a + left + 1, b, i + 1, d - 1)
            return root

        return func(0,len(preorder)-1,0,len(preorder))
        