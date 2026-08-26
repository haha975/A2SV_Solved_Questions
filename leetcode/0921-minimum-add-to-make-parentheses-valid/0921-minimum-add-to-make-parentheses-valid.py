class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(s[i])
            else:
                if stack and stack[-1]=="(":
                    stack.pop()
                elif not stack or stack[-1]==")":
                    stack.append(s[i])
        return len(stack)

        