class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        rev=piles[::-1]
        ans=0
        check=0
        n=len(piles)
        for i in range(n):
            if i%2!=0:
                check+=1
                ans+=rev[i]
            if check==(n/3):
                break
        return ans



        
