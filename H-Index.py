class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        rev=citations[::-1]
        ans=0
        for i in range(len(citations)):
            if rev[i]>=(i+1):
                ans+=1
            else:
                break
            
        return ans

        
