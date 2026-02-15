class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        tup = ((-1,-1), (-1,0), (-1,1),
               (0,1), (1,1), (1,0),
               (1,-1), (0,-1))   
        ans = []
        m = len(img)
        n = len(img[0])       
        for i in range(m):
            row = []
            for j in range(n):
                total = img[i][j]
                count = 1             
                for c in tup:
                    ni = i + c[0]
                    nj = j + c[1]                   
                    if 0 <= ni < m and 0 <= nj < n:
                        total += img[ni][nj]
                        count += 1               
                row.append(total // count)           
            ans.append(row)       
        return ans

        
