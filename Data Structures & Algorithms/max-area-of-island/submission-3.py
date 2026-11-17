class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        def dfs(grid, r, c):
            if (r < 0 or c < 0 or r==ROWS or c==COLS) or (grid[r][c]==0):
                return 0 
            
            grid[r][c] = 0 
            count = 1 # our current spot is VALID, so it must count as 1 on the return. 
            count += dfs(grid, r+1, c)
            count += dfs(grid, r-1, c)
            count += dfs(grid, r, c+1)
            count += dfs(grid, r, c-1)
            return count
        
        max_land = 0 
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    current_land_area = dfs(grid, i, j)
                    if current_land_area > max_land:
                        max_land = current_land_area
        return max_land 