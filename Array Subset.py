#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        a1=Counter(a)
        b1=Counter(b)
        for x in b1:
            if b1[x]>a1[x]:
                return False
        return True
        
        # Your code here
    
    
    
    
