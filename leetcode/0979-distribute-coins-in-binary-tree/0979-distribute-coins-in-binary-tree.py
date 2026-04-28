# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.move=0
        def back(node):
            if not node:
                return 0

            left=back(node.left)
            right=back(node.right)

            self.move+=abs(left)+abs(right)

            return node.val+left+right-1

        back(root)
        return self.move
        