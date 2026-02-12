class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans={}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j not in ans:
                    ans[j]=[matrix[i][j]]
                else:
                    ans[j].append(matrix[i][j])
        answer=list(ans.values())

        return answer
