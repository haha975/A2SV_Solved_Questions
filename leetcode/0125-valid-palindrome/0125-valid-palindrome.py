class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for i in range(len(s)):
            if s[i].isalnum():
                ans+=s[i]
        ans=ans.lower()
        return ans==ans[::-1]
        