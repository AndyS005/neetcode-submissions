class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])
        visited = set()
        self.max_area = 0 

        def dfs(i, j):
            if ((i, j) in visited or
            i < 0 or i > (row -1)
            or j < 0 or j > (cols - 1) or 
            grid[i][j] == 0 ):
                return 0

            visited.add((i,j))

            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        
        for i in range(row):
            for j in range(cols):
                x = dfs(i, j)
                if x > self.max_area:
                    self.max_area = x

        return self.max_area
             
            


        