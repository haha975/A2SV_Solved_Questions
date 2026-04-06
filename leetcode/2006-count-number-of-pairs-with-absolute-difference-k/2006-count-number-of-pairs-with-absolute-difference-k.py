class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        final=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                su=abs(nums[i]-nums[j])
                if su==k:
                    final+=1
        return final

        