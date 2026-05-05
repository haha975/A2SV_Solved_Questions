class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans=[]
        sor=[]
        for num in reversed(nums):
            pos=bisect_left(sor,num)
            ans.append(pos)
            insort(sor,num)
        return ans[::-1]




        