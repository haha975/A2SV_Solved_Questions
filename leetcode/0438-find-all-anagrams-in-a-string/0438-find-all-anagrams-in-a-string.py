
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        p=list(p)
        p.sort()
        k=len(p)
        for i in range(len(s)-k+1):
            check=s[i:i+k]
            check=list(check)
            check.sort()
            if check==p:
                ans.append(i)
        return ans

        
