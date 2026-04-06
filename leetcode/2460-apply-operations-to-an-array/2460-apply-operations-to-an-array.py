class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        final=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                final.append(nums[i])
        cou=nums.count(0)
        lis=[0]*cou
        final=final+lis
        return final
        