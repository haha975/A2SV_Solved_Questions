
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt={}
        for i in strs:
            key="".join(sorted(i))
            if key not in dictt:
                dictt[key]=[]
            dictt[key].append(i)
        return list(dictt.values())


        
