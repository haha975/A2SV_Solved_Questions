class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ptr=0 
        ans=""
        while ptr<len(s):
            ans+=s[ptr:ptr+k][::-1]
            ans+=s[ptr+k:ptr+k+k]
            ptr+=k*2
        return ans






        