t=int(input())
lis=list(map(int,input().split()))
lis.sort()
if len(lis)%2==1:
    idx=len(lis)//2
    print(lis[idx])
else:
    idx=len(lis)//2
    print(lis[idx-1])
