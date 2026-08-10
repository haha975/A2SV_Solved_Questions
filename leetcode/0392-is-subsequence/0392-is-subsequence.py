class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p=0
        pp=0
        if len(s)>len(t):
            return False
        if len(s) == 0:
            return True
            
        while p<len(s) and pp<len(t):
            if s[p]==t[pp] and p==len(s)-1:
                return True
            elif s[p]==t[pp]:
                p+=1
                pp+=1
            elif s[p]!=t[pp]:
                pp+=1
        
        return False


        