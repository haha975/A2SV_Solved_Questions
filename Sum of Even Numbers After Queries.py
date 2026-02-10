class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        c=copy.deepcopy(nums)
        su=sum(x for x in c if x%2==0)
        for i in range(len(queries)):
            d=nums[queries[i][1]]
            nums[queries[i][1]] = nums[queries[i][1]] +queries[i][0]
            if nums[queries[i][1]] %2==0:
                su=su+nums[queries[i][1]] 
            if d%2==0:
                su=su-d
            ans.append(su)
        return ans
