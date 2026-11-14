class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        for right in range(1,len(nums)):
            if nums[left]==0 and nums[right]!=0:
                c=nums[left]
                nums[left]=nums[right]
                nums[right]=c
                left+=1
            elif nums[left]!=0:
                left+=1
            

        