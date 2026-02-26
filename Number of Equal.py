n,m=map(int,input().split())
nl=list(map(int,input().split()))
ml=list(map(int,input().split()))
hash1={}
hash2={}
for i in range(len(nl)):
    if nl[i] not in hash1:
        hash1[nl[i]]=0
    hash1[nl[i]]+=1
for i in range(len(ml)):
    if ml[i] not in hash2:
        hash2[ml[i]]=0
    hash2[ml[i]]+=1
ans=0
if len(nl)>len(ml):
    for key,value in hash1.items():
        if key in hash2:
            ans+=value*hash2[key]
else:
    for key,value in hash2.items():
        if key in hash1:
            ans+=value*hash1[key]
 
 
print(ans)
