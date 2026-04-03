class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        radius = 0
        
        for house in houses:
            i = bisect_left(heaters, house)
            right_dist = float('inf')
            if i < len(heaters):
                right_dist = heaters[i] - house
            
            left_dist = float('inf')
            if i > 0:
                left_dist = house - heaters[i - 1]
            
            closest = min(left_dist, right_dist)
            radius = max(radius, closest)
        
        return radius
        
