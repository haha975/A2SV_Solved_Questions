class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen={0:1}
        prif=[0]*len(nums)
        prif[0]=nums[0]
        ans=0
        for i in range(1,len(nums)):
            prif[i]=prif[i-1]+nums[i]

        for j in range(len(nums)):
            check=prif[j]-k
            if check in seen:
                ans+=seen[check]
            if prif[j] not in seen:
                seen[prif[j]]=1
            else:
                seen[prif[j]]+=1
        return ans
            

        



        

          