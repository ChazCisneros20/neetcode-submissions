class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        visited = set()
        #The goal of the Matrix-BFS/DFS algo
        #is to simply mark all elements as "visited"
        #so the main double-for-loop algo can skip those elements. 
        def dfs(grid, r, c, visited):
            if (r < 0 or c < 0 or r==ROWS or c==COLS) or (grid[r][c]=='0') or ((r,c) in visited):
                return 
            visited.add((r,c))
            dfs(grid,r+1,c, visited)
            dfs(grid,r-1,c, visited)
            dfs(grid,r,c+1, visited)
            dfs(grid,r,c-1, visited)
            return 


        island_count = 0 
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=='1' and (i,j) not in visited:
                    island_count+=1
                    dfs(grid, i, j, visited)
        return island_count