n=int(input())
chil=[[] for _ in range(n+1)]

for i in range(2,n+1):
    p=int(input())
    chil[p].append(i)

isleaf=[False]*(n+1)
for i in range(1,n+1):
    if len(chil[i])==0:
        isleaf[i]=True
for i in range(1,n+1):
    if not isleaf[i]:
        leaf=0
        for c in chil[i]:
            if isleaf[c]:
                leaf+=1
        if leaf<3:
            print("No")
            exit()
print("Yes")