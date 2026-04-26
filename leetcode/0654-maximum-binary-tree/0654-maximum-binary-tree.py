# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_val=max(nums)
        ind=nums.index(max_val)

        root=TreeNode(max_val)
        root.left=self.constructMaximumBinaryTree(nums[:ind])
        root.right=self.constructMaximumBinaryTree(nums[ind+1:])

        return root