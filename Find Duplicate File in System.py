class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans={}
        final=[]
        for i in range(len(paths)):
            pa=list(paths[i].split())
            for j in range(len(pa)):
                if j==0:
                    continue
                else:
                    k=pa[j].index("(")
                    if pa[j][k:] in ans:
                        c=pa[0]+"/"+pa[j][:k]
                        ans[pa[j][k:]].append(c)
                    else:
                        c=pa[0]+"/"+pa[j][:k]
                        ans[pa[j][k:]]=[c]
        for key,value in ans.items():
            if len(value)>1:
               final.append(value)
        return final
        

            




        
