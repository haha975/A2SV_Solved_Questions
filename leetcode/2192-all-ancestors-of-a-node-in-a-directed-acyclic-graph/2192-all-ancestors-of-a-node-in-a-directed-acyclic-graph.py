from collections import deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=[[] for _ in range(n)]
        indegree=[0]*n
        for v,k in edges:
            graph[v].append(k)
            indegree[k]+=1
        ansis=[set() for _ in range(n)]
        q=deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        while q:
            v=q.popleft()
            for k in graph[v]:
                ansis[k].add(v)
                ansis[k].update(ansis[v])
                indegree[k]-=1
                if indegree[k]==0:
                    q.append(k)
        ans=[]
        for i in ansis:
            ans.append(sorted(list(i)))
        return ans
        
        
        
        