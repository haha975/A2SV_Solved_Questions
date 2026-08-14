class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        use=len(nums)
        check=Counter(nums)
        ans=[]
        for i in range(1,use+1):
            if i not in check:
                ans.append(i)
        return ans

        