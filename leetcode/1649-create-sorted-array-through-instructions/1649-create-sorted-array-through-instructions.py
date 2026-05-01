class Solution:
    def createSortedArray(self, instructions):
        MOD = 10**9 + 7
        nums = []
        ans = 0

        def lower_bound(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def upper_bound(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        for x in instructions:
            less = lower_bound(nums, x)             
            greater = len(nums) - upper_bound(nums, x)

            ans = (ans + min(less, greater)) % MOD

            pos = upper_bound(nums, x)
            nums.insert(pos, x)

        return ans