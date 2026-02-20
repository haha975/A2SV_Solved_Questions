from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2==1:
            return []

        changed.sort()
        hash=Counter(changed)
        ans=[]

        for num in changed:
            check=num*2

            if hash[num] == 0:
                continue

            if hash[check] == 0:
                return []
            
            ans.append(num)
            hash[num]-=1
            hash[check]-=1
            
        return ans
