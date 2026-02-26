from collections import Counter
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy=0
        yx=0

        for i in range(len(s1)):
            co=s1[i]+s2[i]
            if co=="xy":
                xy+=1
            elif co=="yx":
                yx+=1
        if (xy + yx) % 2 != 0:
            return -1
        return (xy // 2) + (yx // 2) + 2 * (xy % 2)
        
        
