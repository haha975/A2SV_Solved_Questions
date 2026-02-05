from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars2=Counter(chars)
        ans=0
        for str in words:
            c=Counter(str)
            if c<=chars2:
                ans+=len(str)
        return ans

        
