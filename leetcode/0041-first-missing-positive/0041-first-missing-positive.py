class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ma=abs(max(nums))
        se=set(nums)
        for i in range(1,ma+2):
            if i not in se:
                return i

        