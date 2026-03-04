class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prif=[]
        for i in range(len(nums)):
            if i==0:
                prif.append(nums[i])
            else:
                su=nums[i]+prif[-1]
                prif.append(su)
        mi=min(prif)
        if mi<1:
            return abs(mi)+1
        else:
            return 1
        
