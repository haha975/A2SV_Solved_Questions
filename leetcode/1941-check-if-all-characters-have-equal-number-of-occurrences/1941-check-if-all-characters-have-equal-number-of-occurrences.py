class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        coun=Counter(s)
        c=set()
        for i ,j in coun.items():
            c.add(j)
        print(coun)
        if len(c)==1:
            return True
        return False
        