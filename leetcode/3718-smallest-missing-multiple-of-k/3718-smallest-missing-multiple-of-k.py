class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hash=set(nums)
        nums.sort()
        for i in range(len(nums )+1):
            if k*(i+1) not in hash:
                return k*(i+1)
        



        