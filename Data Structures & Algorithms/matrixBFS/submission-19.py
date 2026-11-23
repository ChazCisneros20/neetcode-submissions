class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[len(grid)-1][len(grid[0])-1]==1 or grid[0][0]==1:
            return -1 
        ROWS,COLS = len(grid), len(grid[0])
        row_dirs = [-1, 1, 0, 0]
        col_dirs = [0, 0, -1, 1]
        visited = set() 
        row_queue=collections.deque()
        col_queue=collections.deque()
        visited.add((0,0)) # this is ensured to be a correct spot. 
        row_queue.append(0)
        col_queue.append(0)

        # the START cell is considered length=0 
        length = 0 
        while len(row_queue) > 0: # or col_queue   
            for i in range(len(row_queue)):
                r,c = row_queue.popleft(), col_queue.popleft()
                # if our current popped node is the END cell, then stop and return the length that cell is at
                if r==ROWS-1 and c==COLS-1:
                    return length
                for i in range(4): # for 4-directions up/down/left/right
                    dr = row_dirs[i]
                    dc = col_dirs[i]
                    if (r+dr<0 or c+dc<0 or r+dr==ROWS or c+dc==COLS) or ((r+dr,c+dc) in visited) or (grid[r+dr][c+dc]==1):
                        continue 
                    visited.add((r+dr,c+dc))
                    row_queue.append(r+dr)
                    col_queue.append(c+dc)
            length+=1
        return -1