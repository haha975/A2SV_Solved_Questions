n,k=map(int,input().split())
lis=list(map(int,input().split()))
seen={}
left=0
best=0
ans=[1,1]
for right in range(len(lis)):
    if lis[right] not in seen:
        seen[lis[right]]=0
    seen[lis[right]]+=1
    
    while len(seen)>k:
        seen[lis[left]]-=1
        if seen[lis[left]]==0:
            del seen[lis[left]]
        left+=1
    po=right-left+1
    if po>best:
        best=po
        ans=[left+1,right+1]
print(*ans)


