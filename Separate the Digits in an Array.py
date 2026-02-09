class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            li=str(nums[i])
            for j in range(len(li)):
                ans.append(int(li[j]))
        return ans
        
