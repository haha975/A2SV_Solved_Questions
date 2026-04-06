class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # count=0
        # citations.reverse()
        # for i in range(len(citations)):
        #     if citations[i]>=i+1:
        #         count+=1
        # return count
        n=len(citations)
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if citations[mid]>=n-mid:
                right=mid-1
            else:
                left=mid+1
        return n-left
        