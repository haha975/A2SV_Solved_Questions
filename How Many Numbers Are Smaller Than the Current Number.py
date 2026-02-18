class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            sum=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    sum+=1
                else:
                    continue
            ans.append(sum)
        return ans

        
