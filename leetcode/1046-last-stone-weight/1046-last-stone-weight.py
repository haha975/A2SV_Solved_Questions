import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            y=-heapq.heappop(stones)
            x=-heapq.heappop(stones)
            if y!=x:
                c=y-x
                heapq.heappush(stones,-c)
        return  -stones[0] if stones else 0
        

        