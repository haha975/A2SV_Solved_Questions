class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}
        for ch in s:
            if ch not in count:
                count[ch]=0
            count[ch]+=1
        result = []
        for ch in order:
            if ch in count:
                result.append(ch * count[ch])
                del count[ch]
        for ch in count:
            result.append(ch * count[ch])
        return "".join(result)

        
