class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mi=deque()
        md=deque()
        ans=0
        left=0

        for right in range(len(nums)):

            while mi and nums[right]<mi[-1]:
                mi.pop()
            mi.append(nums[right])

            while md and nums[right]>md[-1]:
                md.pop()
            md.append(nums[right])

            while md[0] - mi[0] > limit:
                if md[0] == nums[left]:
                    md.popleft()
                if mi[0] == nums[left]:
                    mi.popleft()
                left += 1

            ans=max(ans,right-left+1)
        return ans
            
                


        
