class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        def backt(idx,arr):
            if idx==n:
                ans.append(nums[:])
                return 
            for i in range(idx,n):
                nums[idx],nums[i]=nums[i],nums[idx]
                backt(idx+1,arr)
                nums[idx],nums[i]=nums[i],nums[idx] 
        backt(0,[])
        return ans
            
        
