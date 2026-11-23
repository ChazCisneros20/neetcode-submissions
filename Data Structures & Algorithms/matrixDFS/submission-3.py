class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        if grid[0][0]==1 or grid[ROWS-1][COLS-1]==1:
            return 0 
        visited = set()
        # up/down/left/right
        row_dirs = [-1, 1, 0, 0]
        col_dirs = [0, 0, -1, 1]
        
        def dfs(grid, r, c, visited):
            if (r<0 or c<0 or r==ROWS or c==COLS) or (grid[r][c]==1) or ((r,c) in visited):
                return 0 
            if (r==ROWS-1 and c==COLS-1):
                return 1
            visited.add((r,c))
            count=0
            for i in range(4):
                count += dfs(grid, r+row_dirs[i], c+col_dirs[i], visited)
            visited.remove((r,c))
            return count

        return dfs(grid, 0, 0, visited) 