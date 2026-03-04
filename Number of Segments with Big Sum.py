n,s=map(int,input().split())
lis=list(map(int,input().split()))
cur_sum=0
ans=0
right=0
for left in range(n):
    while cur_sum<s and right<n:
        cur_sum+=lis[right]
        right+=1
    if cur_sum>=s: 
        ans+= n-right+1 
    cur_sum -=lis[left] 
    
print(ans)

