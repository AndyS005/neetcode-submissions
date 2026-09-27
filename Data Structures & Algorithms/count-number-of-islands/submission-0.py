class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        counter = 0
        
        def dfs(i, j):
            if ( i >= rows or j >= cols or i < 0 or j < 0 or 
            grid[i][j] == "0" or
            (i, j) in visited):
                return 

            visited.add((i,j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i, j)
                    counter += 1

        return counter



            
            

