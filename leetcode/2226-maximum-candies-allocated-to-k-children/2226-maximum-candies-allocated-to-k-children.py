class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left=1
        right=max(candies)
        ans=0
        while left<=right:
            mid=(left+right)//2
            total=0
            for i in range(len(candies)):
                total += candies[i] //mid
            if total>=k:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans

        