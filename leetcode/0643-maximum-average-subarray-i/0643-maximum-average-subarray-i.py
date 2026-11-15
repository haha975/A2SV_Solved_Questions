class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        first=sum(nums[:k])
        ma=first/k
        for i in range(k,len(nums)):
            first-=nums[i-k]
            first+=nums[i]
            ma=max(ma,first/k)
        return ma



        