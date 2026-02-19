
n=int(input())
lis=list(map(int,input().split()))
lis.sort()
ans=1
for x in lis:
    if x >= ans:
        ans += 1
print(ans-1)
