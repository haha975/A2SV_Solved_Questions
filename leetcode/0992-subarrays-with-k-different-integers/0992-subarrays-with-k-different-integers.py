class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            left = 0
            seen = defaultdict(int)
            ans = 0
            
            for right in range(len(nums)):
                seen[nums[right]] += 1
                
                if seen[nums[right]] == 1:
                    k -= 1
                
                while k < 0:
                    seen[nums[left]] -= 1
                    if seen[nums[left]] == 0:
                        k += 1
                    left += 1
                
                ans += right - left + 1
            
            return ans
        
        return atMost(k) - atMost(k - 1)
                

        