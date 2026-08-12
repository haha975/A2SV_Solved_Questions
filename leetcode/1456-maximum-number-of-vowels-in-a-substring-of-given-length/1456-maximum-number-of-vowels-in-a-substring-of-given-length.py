class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans=0
        voil = ["a", "e", "i", "o", "u"]
        for i in range(k):
            if s[i] in voil:
                ans+=1
        check=ans
        for i in range(1,len(s)-k+1):
            if s[i-1] in voil:
                check-=1
            if s[i+k-1] in voil:
                check+=1
            if check>ans:
                ans=check

        return ans



        