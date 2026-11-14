class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        from collections import deque
         
        visited = set()

        def bfs(grid, r, c):
            #The first position passed is ensured to be an island that ISNT visited
            queue = deque()
            queue.append([r,c])
            while len(queue) > 0:
                for i in range(len(queue)):
                    value = queue.popleft()
                    r,c = value[0], value[1]
                    visited.add((r,c))
                    if (r+1 >= 0 and r+1 < ROWS) and (grid[r+1][c]=='1') and ((r+1,c) not in visited):
                        queue.append([r+1,c])
                        visited.add((r+1,c))
                    if (r-1 >= 0 and r-1 < ROWS) and (grid[r-1][c]=='1') and ((r-1,c) not in visited):
                        queue.append([r-1,c])
                        visited.add((r-1,c))
                    if (c+1 >= 0 and c+1 < COLS) and (grid[r][c+1]=='1') and ((r,c+1) not in visited):
                        queue.append([r,c+1])
                        visited.add((r,c+1))
                    if (c-1 >= 0 and c-1 < COLS) and (grid[r][c-1]=='1') and ((r,c-1) not in visited):
                        queue.append([r,c-1])
                        visited.add((r,c-1))
                
                    

            
        island_count = 0 

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(grid, i, j)
                    island_count+=1 
        return island_count 
                    
                    


