class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mi=max(weights)
        ma=sum(weights)
        while mi<=ma:
            mid=(mi+ma)//2
            ans=0
            check=1
            for i in range(len(weights)):
                if ans+weights[i]>mid:
                    check+=1
                    ans=0
                ans+=weights[i]
            if check<=days:
                ma=mid-1
            else:
                mi=mid+1
        return mi








        