class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        max_area = 0 

        def dfs(r, c):

            if (r < 0 or r >= rows or c < 0 or c >= columns or (r, c) in visited or grid[r][c] == 0):
                return 0 
            
            visited.add((r, c))
            
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) +  dfs(r, c - 1)

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(dfs(i, j), max_area)

        
        return max_area
                

            


        