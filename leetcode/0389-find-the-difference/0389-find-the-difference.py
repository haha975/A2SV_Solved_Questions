class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        check=Counter(s)
        for i in range(len(t)):
            if t[i] not in check:
                return t[i]
            else:
                check[t[i]]-=1
                if check[t[i]]==0:
                    del check[t[i]]
        