class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        hashh={}
        ans=0
        for right in range(len(s)):
            if s[right] not in hashh:
                hashh[s[right]]=0
            hashh[s[right]]+=1
            ma=max(hashh.values())
            max_len=right-left+1
            sum=max_len-ma
            if sum>k:
                hashh[s[left]]-=1
                if hashh[s[left]]==0:
                    del hashh[s[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans
            
        
        
       
        
        


        
