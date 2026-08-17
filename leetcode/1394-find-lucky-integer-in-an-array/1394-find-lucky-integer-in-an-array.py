class Solution:
    def findLucky(self, arr: List[int]) -> int:
        coun=Counter(arr)
        ans=[]
        for key,val in coun.items():
            if val==key:
                ans.append(key)
        ans.sort()
        if ans :
            return ans[-1]
        else:
            return -1
        