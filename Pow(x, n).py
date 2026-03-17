import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==1:
            return x
        if n==0:
            return 1
        x=pow(x,n-1)*x
        return x

        
