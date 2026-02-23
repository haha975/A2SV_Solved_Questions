class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            poi = 0
            while poi < n and haystack[i + poi] == needle[poi]:
                poi += 1
            if poi == n:
                return i

        return -1
