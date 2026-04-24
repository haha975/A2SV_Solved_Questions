class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1 for _ in range(n)]
        result = True

        def dfs(node):
            temp = True
            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    if color[node] == 0:
                        color[neighbour] = 1
                    else:
                        color[neighbour] = 0
                    temp = temp and dfs(neighbour)
                elif color[neighbour] == color[node]:
                    return False
            return temp

        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                result = result and dfs(node)

        return result