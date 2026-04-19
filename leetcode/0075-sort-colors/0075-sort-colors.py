class Solution:
    from collections import Counter
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num=Counter(nums)
        i=0
        for _ in range(num[0]):
            nums[i] = 0
            i += 1
        
        for _ in range(num[1]):
            nums[i] = 1
            i += 1
        
        for _ in range(num[2]):
            nums[i] = 2
            i += 1
        
        
