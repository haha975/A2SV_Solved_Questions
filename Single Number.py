from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq=Counter(nums)
        for num,frq in freq.items():
            if frq==1:
                return num
        
