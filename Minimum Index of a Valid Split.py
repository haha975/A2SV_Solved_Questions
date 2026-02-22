from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count=Counter(nums)
        ma=max(list(count.values()))
        need=0
        for key,value in count.items():
            if value==ma:
                need=key
                break
        check=0
        total=count[need]
        for i in range(len(nums)):
            if nums[i]==need:
                check+=1
            if check*2>i+1 and (total - check) * 2 > len(nums) - i - 1:
                return i
        return -1


        
