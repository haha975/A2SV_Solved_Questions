class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        lengh=len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            left,right=i+1,len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum==target:
                    return sum
                elif abs(sum-target)<abs(ans-target):
                    ans=sum
                if sum<target:
                    left+=1
                else:
                    right-=1
        return ans


