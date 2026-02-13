class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sp = s.split()
        hashh = {}
        used = set()

        if len(pattern) != len(sp):
            return False

        for i in range(len(sp)):
            if pattern[i] not in hashh:
                if sp[i] in used:
                    return False
                hashh[pattern[i]] = sp[i]
                used.add(sp[i])
            else:
                if hashh[pattern[i]] != sp[i]:
                    return False
        return True
