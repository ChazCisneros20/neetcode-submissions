class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        visited = set() #our Matrix-DFS hashSet() 
        row_dirs = [-1,1,0,0]
        col_dirs = [0,0,-1,1]
        def dfs(grid, r, c, visited):
            if (r<0 or c<0 or r==ROWS or c==COLS) or ((r,c) in visited) or (grid[r][c]==0):
                return 0  
            visited.add((r,c))
            count = 1
            for i in range(4):
                dr, dc = row_dirs[i], col_dirs[i]
                count += dfs(grid, r+dr, c+dc, visited)
            return count 

        max_area = 0 
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j]==1:
                    area = dfs(grid, i, j, visited)
                    if area > max_area:
                        max_area = area 
        return max_area