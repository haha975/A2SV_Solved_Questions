class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        hashh = {}
        for i in range(len(s)):
            hashh[s[i]] = i
        ans = []
        p1 = 0
        p2 = 0
        for i in range(len(s)):
            p2 = max(p2, hashh[s[i]])
            if i == p2:
                ans.append(p2 - p1 + 1)
                p1 = i + 1

        return ans
