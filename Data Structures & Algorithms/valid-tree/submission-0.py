class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        if len(edges) != n - 1:
            return False

        visited = set()

        def dfs(node):
            if (node in visited):
                return 

            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour)

            return True

        dfs(0)
        return len(visited) == n

        


        