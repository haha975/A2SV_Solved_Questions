class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        for _ in range(4): 
            if mat == target:
                return True
            hashh = {}
            for i in range(len(mat) - 1, -1, -1):
                for j in range(len(mat[i]) - 1, -1, -1):
                    if j not in hashh:
                        hashh[j] = [mat[i][j]]
                    else:
                        hashh[j].append(mat[i][j])

            mat = list(hashh.values())
            mat.reverse()
