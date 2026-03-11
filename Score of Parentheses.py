class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(s[i])
            elif stack and s[i]==")" and stack[-1]=="(":
                stack.pop()
                stack.append(1)
                if len(stack)>1 and  stack[-2]!="(" and stack[-1]!="(":
                    ans=stack[-2]+stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(ans)


            elif stack and s[i]==")" and stack[-1]!="(":
                ap=stack.pop()*2
                stack.pop()
                if stack and stack[-1]!="(":
                    ans=ap+stack[-1]
                    stack.pop()
                    stack.append(ans)
                else:
                    stack.append(ap)

           
        return stack[0]



        
