class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        st="$".join(source)
        ans=""
        i=0
        while i<len(st):
            if  i + 1 < len(st) and st[i]=="/" and st[i+1]=="/":
                while i < len(st) and st[i]!="$":
                    i+=1
                           
            elif  i + 1 < len(st) and st[i]=="/" and st[i+1]=="*":
                i+=2
                while  i + 1 < len(st) and not (st[i] == "*" and st[i + 1] == "/"):
                    i+=1
                i+=2
            else:
                ans+=st[i]
                i+=1
        
        return [i for i in ans.split("$") if i]
