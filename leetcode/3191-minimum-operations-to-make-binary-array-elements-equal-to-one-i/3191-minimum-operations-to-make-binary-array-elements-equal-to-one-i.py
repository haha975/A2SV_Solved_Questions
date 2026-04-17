class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            if nums[i]!=1 and i<len(nums)-2:
                ans+=1
                nums[i]=1
                if nums[i+1]==0:
                    nums[i+1]=1
                elif nums[i+1]==1:
                    nums[i+1]=0
                if nums[i+2]==0:
                    nums[i+2]=1
                elif nums[i+2]==1:
                    nums[i+2]=0
            elif i>=len(nums)-2:
                break
        if 0 not in nums:
            return ans
        else:
            return -1
            



                



        