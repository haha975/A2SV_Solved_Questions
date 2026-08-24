class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num=Counter(nums)
        lis=[]
        for i,j in num.items():
            if j==1:
                lis.append(i)
        return sum(lis)
        