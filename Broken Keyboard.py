t=int(input())
for i in range(t):
    s=input()
    ans=""
    i=0
    while i<len(s):
        if i + 1 < len(s) and s[i]==s[i+1]:
            i+=2
        else:
            ans+=s[i]
            i+=1
    ans=list(set(ans))
    ans.sort()
    print("".join(ans))

            
