class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        row_dirs = [-1,1,0,0]
        col_dirs = [0,0,-1,1]

        def dfs(grid, r, c, visited):
            if (r<0 or c<0 or r==ROWS or c==COLS) or ((r,c) in visited) or (grid[r][c]=='0'):
                return 
            visited.add((r,c))
            for i in range(4):
                dr = row_dirs[i]
                dc = col_dirs[i]
                dfs(grid, r+dr, c+dc, visited)


        island_count=0
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j]=='1':
                    island_count+=1
                    dfs(grid, i, j, visited)
        return island_count