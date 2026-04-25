import sys
from sys import stdin
from collections import Counter

alp = "abcdefghijklmnopqrstuvwxyz"

tt = int(stdin.readline())
ANS = []

for loop in range(tt):

    s = input().strip()
    t = input().strip()

    slis = Counter(s)
    tlis = Counter(t)

    flag = True
    for c in slis:
        if slis[c] > tlis[c]:
            flag = False
            break

    if not flag:
        ANS.append("Impossible")
        continue

    for c in s:
        tlis[c] -= 1
    cnt = [0] * 26
    for c in tlis:
        cnt[ord(c) - ord('a')] = tlis[c]

    tlis = cnt
    ans = []

    srem = list(s)
    srem.reverse()

    for i in range(26):
        while len(srem) > 0 and srem[-1] <= alp[i]:
            ans.append(srem.pop())
        while tlis[i] > 0:
            ans.append(alp[i])
            tlis[i] -= 1

    ANS.append("".join(ans))

print(*ANS, sep="\n")