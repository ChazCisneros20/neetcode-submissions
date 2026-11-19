class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1 
        if grid[len(grid)-1][len(grid[0])-1]==1:
            return -1 
        # Init your variables Data Science style 
        ROWS,COLS = len(grid), len(grid[0])
        neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
        row_directions = [0, 0, 1, -1]
        col_directions = [1, -1, 0, 0]
        visited = set() 
        row_queue = collections.deque()
        col_queue = collections.deque() 
        row_queue.append(0)
        col_queue.append(0)

        length = 0 
        while len(row_queue) > 0: # or col_queue 
            for i in range(len(row_queue)):
                r = row_queue.popleft()
                c = col_queue.popleft()
                if ((r==ROWS-1) and (c==COLS-1)):
                    return length
                for i in range(4):
                    dr = row_directions[i]
                    dc = col_directions[i]
                    if (r+dr<0 or c+dc<0 or r+dr==ROWS or c+dc==COLS) or ((r+dr,c+dc) in visited) or (grid[r+dr][c+dc]==1):
                        continue 
                    #else:
                    visited.add((r+dr, c+dc))
                    row_queue.append(r+dr)
                    col_queue.append(c+dc)
            #each breadth, for each direction, will have length+=1 
            length+=1 
        return -1 
                
        