class Solution:    
    def findUnion(self, a, b):
        ans=a+b
        c=list(set(ans))
        c.sort()
        return c
        # code here
