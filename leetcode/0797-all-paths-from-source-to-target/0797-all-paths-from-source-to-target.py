class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        tar=len(graph)-1

        def back(node,path):
            if node==tar:
                ans.append(path[:])
                return
            for i in graph[node]:
                path.append(i)
                back(i,path)
                path.pop()



        back(0,[0])
        return ans
        


        