class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c=Counter(s)
        d=Counter(t)
        ans=list((c-d).values())
        return sum(ans)
