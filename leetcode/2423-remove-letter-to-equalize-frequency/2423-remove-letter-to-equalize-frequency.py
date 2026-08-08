class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            wor=word[:i]+word[i+1:]
            coun=Counter(wor)
            ans=set(coun.values())
            if len(ans)==1:
                return True
        return False
        

        