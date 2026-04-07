class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
   
            return merge(left_half,right_half)

        def merge(left_half,right_half):
            ptr1 = 0
            ptr2 = 0
            ans = []
            while ptr1 < len(left_half) and ptr2 < len(right_half):
                if left_half[ptr1] < right_half[ptr2]:
                    ans.append(left_half[ptr1])
                    ptr1 += 1
                else:
                    ans.append(right_half[ptr2])
                    ptr2 += 1
            while ptr1 < len(left_half):
                ans.append(left_half[ptr1])
                ptr1 += 1

            while ptr2 < len(right_half):
                ans.append(right_half[ptr2])
                ptr2 += 1

            return ans

        return mergeSort(0, len(nums) - 1, nums)
        