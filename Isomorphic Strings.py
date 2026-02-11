from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st={}
        ts={}
        if len(s)!=len(t):
            return False
        else:
            for s1,s2 in zip(s,t):
                if s1 in st and st[s1]!=s2:
                    return False
                if s2 in ts and ts[s2]!=s1:
                    return False
                st[s1]=s2
                ts[s2]=s1
        return True  
