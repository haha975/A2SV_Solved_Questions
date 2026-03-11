n,k=map(int,input().split())
lis=list(map(int,input().split()))
seen={}
check=0
left=0
ans=0

for right in range(len(lis)):
    if lis[right] not in seen:
        seen[lis[right]]=0
    seen[lis[right]]+=1

    while len(seen)>k:
        seen[lis[left]]-=1
        if seen[lis[left]]==0:
            del seen[lis[left]]
        left+=1
    ans+=right-left+1

print(ans)
