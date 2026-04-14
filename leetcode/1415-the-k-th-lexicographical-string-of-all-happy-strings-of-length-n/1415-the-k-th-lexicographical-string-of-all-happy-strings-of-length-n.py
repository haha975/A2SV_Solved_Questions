class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res=[]
        def back(s):
            if len(res)==k:
                return
            if len(s)==n:
                res.append(s)
                return
            for b in ["a","b","c"]:
                if not s or s[-1]!=b:
                    back(s+b)

        back("")
        return res[k-1] if len(res)>=k else ""
        