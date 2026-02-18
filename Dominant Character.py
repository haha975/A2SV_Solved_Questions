t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = n + 1 
    for i in range(n):
        a = b = c = 0
        for j in range(i, n):
            if s[j] == 'a':
                a += 1
            elif s[j] == 'b':
                b += 1
            else:
                c += 1  
            if j - i + 1 >= 2 and a > b and a > c:
                ans = min(ans, j - i + 1)
                break 
    print(-1 if ans == n + 1 else ans)
