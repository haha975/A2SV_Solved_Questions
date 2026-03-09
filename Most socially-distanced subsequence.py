t=int(input())
for _ in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    ans=[]
    ans.append(lis[0])
    for i in range(1,n-1):
        if (lis[i]<lis[i-1] and lis[i]<lis[i+1]) or (lis[i]>lis[i-1] and lis[i]>lis[i+1]):
            ans.append(lis[i])
    ans.append(lis[-1])
    print(len(ans))
    print(*ans)
