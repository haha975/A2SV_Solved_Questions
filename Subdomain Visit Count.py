class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashh={}
        ans=[]
        for i in cpdomains:
            li=list(i.split())
            c=li[1].split('.')
            listt=[li[0]] + ['.'.join(c[i:]) for i in range(len(c))]
            for j in range(len(listt)):
                if j==0:
                    continue
                elif listt[j] not in hashh:
                    hashh[listt[j]]=int(listt[0])
                else:
                    hashh[listt[j]]+=int(listt[0])
        for key,value in hashh.items():
            ans.append(str(value)+" "+key)
        return ans


        
                


        
