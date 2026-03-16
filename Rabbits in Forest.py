from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        check=Counter(answers)
        ans=0
        for key,value in check.items():
            if value<=key+1:
                ans+=key+1
            else:
                groups = (value + key) // (key + 1)
                ans += groups * (key + 1)
                       
        return ans
            



        
        
