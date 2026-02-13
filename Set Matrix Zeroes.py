class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowss=set()
        colss=set()
        def ro(row,col):
            
            rows=set()
            cols=set()
            for c in range(len(matrix[0])):
                rows.add((i,c))
            for d in range(len(matrix)):
                cols.add((d,j))
            return [rows,cols]
            

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    
                    dd=ro(i,j)
                    rowss.update(dd[0])
                    colss.update(dd[1])
        for i in rowss:
            matrix[i[0]][i[1]]=0
        for i in colss:
            matrix[i[0]][i[1]]=0

        
        


        
            
        







        

        
