class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n= len(mat),len(mat[0])
        c=m+n-1
        hashh={}
        ans=[]
        for i in range(m):
            for j in range(n):
                d = i + j
                if d not in hashh:
                    hashh[d] = []
                hashh[d].append(mat[i][j])
        for d in range(c):
            if d%2==0:
                ans.extend(hashh[d][::-1])
            else:
                ans.extend(hashh[d])
        return ans

        
                    
        
