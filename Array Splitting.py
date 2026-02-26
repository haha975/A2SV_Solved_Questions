n,s=map(int,input().split())
lis=list(map(int,input().split()))
if s==1:
    print(lis[len(lis)-1]-lis[0])
elif s==n:
    print(0)
else:
    gaps = []
    for i in range(1, n):
        gaps.append(lis[i] - lis[i - 1])

    gaps.sort(reverse=True)
    print(lis[-1] - lis[0] - sum(gaps[:s - 1]))
    
