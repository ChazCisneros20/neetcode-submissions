class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c, visited):
            ROWS = len(grid)
            COLS = len(grid[0])
            #BASE CASE 1: Invalid placement. 
            if (r < 0 or c < 0 or r==ROWS or c==COLS) or (r,c) in visited or grid[r][c]==1:
                return 0 
            #BASE CASE 2: Valid. Reached bottom-rightmost
            if r==ROWS-1 and c==COLS-1:
                return 1 
            visited.add( (r,c) )
            currentCount = 0 
            currentCount += dfs(grid, r+1, c, visited)
            currentCount += dfs(grid, r-1, c, visited)
            currentCount += dfs(grid, r, c+1, visited)
            currentCount += dfs(grid, r, c-1, visited)

            #return to prior placement, so remove this current placement
            visited.remove( (r,c) )
            #return the count of paths this current placement spawned. 
            return currentCount 
        
        return dfs(grid, 0, 0, set())
