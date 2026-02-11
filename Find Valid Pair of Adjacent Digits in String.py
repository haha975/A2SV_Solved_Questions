from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        c=Counter(s)
        for i in range(len(s)-1):
            a,b=s[i],s[i+1]
            if a!=b and int(a)==c[a] and int(b)==c[b] :
                return a+b
        return ""
