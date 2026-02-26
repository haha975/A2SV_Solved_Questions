class Solution:
    def frequencySort(self, s: str) -> str:
        hashh={}
        for i in range(len(s)):
            if s[i] not in hashh:
                hashh[s[i]]=0
            hashh[s[i]]+=1
     
        count=list(hashh.values())
        count.sort(reverse=True)
        s=list(s)
        s.sort()
        ans=""
        for i in range(len(count)):
            for key,value in hashh.items():
                if value==count[i]:
                    ans+=key*value
                    hashh[key]="$"
                    break
        return ans



        
            








        
