class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        for i in range(len(responses)):
            responses[i]=list(set(responses[i]))
        hashh={}
        ans=[]
    
        for i in range(len(responses)):
            ans.extend(responses[i])
        
        ans.sort()

        for i in range(len(ans)):
            if ans[i] not in hashh:
                hashh[ans[i]]=0
            hashh[ans[i]]+=1
        
        c=list(hashh.values())  
        ma=max(c)  
        for i in range(len(ans)):
            if hashh[ans[i]]==ma:
                return ans[i]
