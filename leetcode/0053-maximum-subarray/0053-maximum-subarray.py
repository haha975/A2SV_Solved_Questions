class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prifix=[]
        for i in range (len(nums)):
            if not prifix:
                prifix.append(nums[i])
            else:
                prifix.append(nums[i]+prifix[-1])
        minp=0
        ans=float(-inf)
        for j in range(len(prifix)):
            ans=max(ans,prifix[j]-minp)
            minp=min(minp,prifix[j])
        return ans


        
        


        