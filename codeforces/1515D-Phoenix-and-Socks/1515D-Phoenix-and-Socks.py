import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    c = list(map(int, input().split()))

    from collections import defaultdict

    left = defaultdict(int)
    right = defaultdict(int)
    for i in range(l):
        left[c[i]] += 1
    for i in range(l, n):
        right[c[i]] += 1

    for color in list(left.keys()):
        match = min(left[color], right[color])
        left[color] -= match
        right[color] -= match

    left_total = sum(left.values())
    right_total = sum(right.values())

    if left_total > right_total:
        left, right = right, left
        left_total, right_total = right_total, left_total

    diff = (right_total - left_total) // 2
    cost = 0


    for color in right:
        cnt = right[color]
        take = min(diff, cnt // 2)
        cost += take
        diff -= take
        right[color] -= take * 2


    cost += diff

    remaining = sum(left.values()) + sum(right.values())
    cost += remaining // 2

    print(cost)