class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen={0:1}
        total=0
        ans=0

        for j in range(len(nums)):
            total+=nums[j]
            a=total-k
            if a in seen:
                ans+=seen[a]
            if total not in seen :
                seen[total]=1
            else:
                seen[total]+=1

        return ans

          