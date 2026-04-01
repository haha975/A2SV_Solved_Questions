t=int(input())
for _ in range(t):
    n,x,k=map(int,input().split())
    s=input()
    move=[1 if i=="R" else -1 for i in s]

    pos=x
    first=-1
    for i in range(len(s)):
        pos+=move[i]
        if pos==0:
            first=i+1
            break
    
    if first==-1 or first>k:
        print(0)
        continue
    pos=0
    cycle=-1
    for i in range(n):
        pos+=move[i]
        if pos==0:
            cycle=i+1
            break
    if cycle==-1 :
        print(1)
    else:
        remain=k-first
        print(1+remain//cycle)