class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1=list(Counter(word1).values())
        c2=list(Counter(word2).values())
        c1.sort()
        c2.sort()
        d=list(set(list(word1)))
        d2=list(set(list(word2)))
        d.sort()
        d2.sort()
        
        if d!=d2:
            return False
        else:
            if c1==c2:
                return True
            else:
                return False
