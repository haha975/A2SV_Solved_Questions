class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        pre=[0]*len(nums)
        pre[0]=nums[0]
        suf=[0]*len(nums)
        suf[-1]=nums[-1]
        for i in range(1,len(nums)):
            pre[i]=pre[i-1]+nums[i]
        for i in range(len(nums)-2,-1,-1):
            suf[i]=suf[i+1]+nums[i]
        print(suf)
        print(pre)
        for j in range(len(nums)):
            if suf[j]==pre[j]:
                return j
        return -1
        

        