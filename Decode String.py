class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                check=""
                while stack[-1] != "[":
                    check = stack.pop()+check
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                ans = int(num) * check
                stack.append(ans)
        return "".join(stack)

            
            
        
