class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash={0:1}
        prif=0
        count=0
        for i in range(len(nums)):
            prif+=nums[i]
            
            if (prif-k) in hash:
                count+=hash[prif-k]
            if prif in hash:
                hash[prif]+=1
            else:
                hash[prif]=1
        return count





        