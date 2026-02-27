t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    lis=[]
    for j in range(n):
        c=list(map(int,input().split()))
        lis.append(c)
    lis.sort()
    for f in range(len(lis)):
        if lis[f][2]>=k and k>=lis[f][0] and k<=lis[f][1]:
            k=lis[f][2]
    print(k)
