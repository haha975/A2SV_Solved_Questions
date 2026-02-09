import math
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=math.floor(len(nums)/3)
        d=Counter(nums)
        ans=[]
        for key,value in d.items():
            if value>c:
                ans.append(key)
        return ans
        
        
