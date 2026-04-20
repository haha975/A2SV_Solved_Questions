class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        nums.sort()
        ma=0
        for i in range(len(nums)-1):
            dif=nums[i+1]-nums[i]
            ma=max(ma,dif)
        if ma<2 and len(nums)<2:
            return 0
        return ma
