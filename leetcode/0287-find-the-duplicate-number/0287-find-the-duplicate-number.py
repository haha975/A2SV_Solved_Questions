from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cont=Counter(nums)
        for k,v in cont.items():
            if v>=2:
                return k

        