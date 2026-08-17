class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sum=s1+" "+s2
        sum=sum.split(" ")
        coun=Counter(sum)
        ans=[]
        for key,val in coun.items():
            if val<2:
                ans.append(key)
        return ans
        