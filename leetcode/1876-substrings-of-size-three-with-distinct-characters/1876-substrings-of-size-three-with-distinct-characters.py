class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans=0
        for i in range(len(s)-1):
            check=s[i:i+3]
            if len(set(check))==3:
                ans+=1
        return ans

        