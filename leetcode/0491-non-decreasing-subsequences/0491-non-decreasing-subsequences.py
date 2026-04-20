class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        def back(nums,idx,lis):
            if len(lis)>=2:
                ans.add(tuple(lis))
            for i in range(idx,len(nums)):
                if not lis or nums[i]>=lis[-1]:
                    back(nums,i+1,lis+[nums[i]])
        back(nums,0,[])
        return list(ans)


        