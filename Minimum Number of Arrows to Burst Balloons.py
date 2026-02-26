class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        check = points[0][1]
        hashh={}
        for i in range(len(points)):
            if check<=points[i][1] and check>=points[i][0]:
                if check not in hashh:
                    hashh[check]=0
                hashh[check]+=1
            else:
                check=points[i][1]
                if check not in hashh:
                    hashh[check]=0
                hashh[check]+=1

        c =list(hashh.values())
        return len(c)
        

        
