class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        if nums==sorted(nums):
            return 0
        limit=0
        op=0
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                limit=nums[i]
            if nums[i]>limit:
                k=ceil(nums[i]/limit)
                op+=(k-1)
                limit=nums[i]//k
            elif nums[i]<limit:
                limit=nums[i]
        return op

        
        
