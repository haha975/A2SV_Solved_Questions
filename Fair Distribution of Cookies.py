class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.mi=float("inf")
        c=[0]*k
        if len(cookies)==1:
            return cookies[0]
        def back(idx):
            if idx==len(cookies):
                self.mi=min(self.mi,max(c))
                return 
        
            for i in range(k):
                if c[i]>self.mi:
                    return
                c[i]+=cookies[idx]
                back(idx+1)
                c[i]-=cookies[idx]
                if c[i]==0:
                    return   
        back(0)
        return self.mi


                
        
