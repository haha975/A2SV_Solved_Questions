a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a3=list(map(int,input().split()))
a4=list(map(int,input().split()))
a5=list(map(int,input().split()))
ans=0

if 1 in a1:
    ans+=2
    c=a1.index(1)+1
    ans+=abs(c-3)

elif 1 in a2:
    ans+=1
    c=a2.index(1)+1
    ans+=abs(c-3)

elif 1 in a3:
    c=a3.index(1)+1
    ans+=abs(c-3)

elif 1 in a4:
    ans+=1
    c=a4.index(1)+1
    ans+=abs(c-3)

elif 1 in a5:
    ans+=2
    c=a5.index(1)+1
    ans+=abs(c-3)

print(ans)
