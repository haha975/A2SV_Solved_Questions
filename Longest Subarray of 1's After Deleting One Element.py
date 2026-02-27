class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        hash={}
        left=0
        ans=0
        for right in range(len(nums)):
            if nums[right] not in hash:
                hash[nums[right]]=0
            hash[nums[right]]+=1
            ma=0
            if 1 in hash:
                ma=hash[1]
            max_len=right-left+1
            if max_len-ma>1:
                hash[nums[left]]-=1
                if hash[nums[left]]==0:
                    del hash[nums[left]]
                left+=1
            ans=max(ans,right-left)
        return ans
    
        
