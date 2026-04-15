from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        coun=Counter(nums)
        ans=[]
        for k,v in coun.items():
            if v==2:
                ans.append(k)
        for i in range(1,len(nums)+1):
            if i not in coun:
                ans.append(i)
                return ans


        