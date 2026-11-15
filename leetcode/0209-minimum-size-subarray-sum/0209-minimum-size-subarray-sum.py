class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        sum=0
        coun=float('inf')
        for right in range(len(nums)):
            sum+=nums[right]
            while left<=right and sum>=target:
                sum-=nums[left]
                coun=min(coun,right-left+1)
                left+=1
        return 0 if coun == float('inf') else coun





            

        