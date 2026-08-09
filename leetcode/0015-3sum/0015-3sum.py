class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        num=sorted(nums)
        ans=[]
        for i in range(len(nums)):
            if i > 0 and num[i] == num[i - 1]:
                continue
            left, right = i + 1, len(num) - 1
            k = 0 - num[i]
            while left < right:
                if num[left] + num[right] == k:
                    ans.append([num[i], num[left], num[right]])
                    left += 1
                    right -= 1
                    while left < right and num[left] == num[left - 1]:
                        left += 1
                    while left < right and num[right] == num[right + 1]:
                        right -= 1
                elif num[left] + num[right] < k:
                    left += 1
                else:
                    right -= 1

        return ans



        
        