t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=list(input())
    ma=float('inf')
    left=0
    check=0
    for right in range(n):
        if s[right]=="W":
                check+=1
        if right-left+1==k:
            ma=min(ma,check)
            if s[left]=="W":
                check-=1
                left+=1
            else:
                left+=1
        
    print(ma)




    



