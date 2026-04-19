class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,k in enumerate(nums):
            dif=target-k
            
            if dif in hash:
                return [hash[dif][0],i]
            if k not in hash:
                hash[k]=[]
            hash[k].append(i)
        
        # nums.sort()

        # left=0
        # right=len(nums)-1
        
        # while left<right:
        #     su=nums[left]+nums[right]
        #     if su==target:
        #         c=hash[nums[left]][0]
        #         hash[nums[left]].pop(0)
        #         d=hash[nums[right]][0]
        #         return [c,d]
        #     elif su>target:
        #         right-=1
        #     elif su<target:
        #         left+=1 


    
      

        
        