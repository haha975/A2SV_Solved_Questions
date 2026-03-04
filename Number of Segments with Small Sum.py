n,s=map(int,input().split())
lis=list(map(int,input().split()))
cur_sum=0
ans=0
right=0
for left in range(n):
    while right<n and cur_sum+lis[right]<=s:
        cur_sum+=lis[right]
        right+=1
    ans += right - left
    cur_sum -=lis[left] 
    
print(ans)

