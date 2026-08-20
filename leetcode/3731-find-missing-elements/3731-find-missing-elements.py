class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ma=max(nums)
        mi=min(nums)
        lis=[]
        nums=set(nums)
        for i in range(mi,ma+1):
            lis.append(i)
        ans=[]
        for i in range(len(lis)):
            if lis[i] not in  nums:
                ans.append(lis[i])
        return ans
        