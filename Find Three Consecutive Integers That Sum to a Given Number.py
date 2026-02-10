class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans=[]
        if num%3==0:
            c=int(num/3)
            ans.append(c-1)
            ans.append(c)
            ans.append(c+1)
        return ans
