class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[len(grid)-1][len(grid[0])-1]==1:
            return -1 
        ROWS,COLS = len(grid), len(grid[0])
        # up/down/left/right up-right/down-left/up-left/down-right
        row_dirs = [-1, 1, 0, 0, -1, 1, -1, 1]
        col_dirs = [0, 0, -1, 1, 1, -1, -1, 1]
        
        row_queue=collections.deque()
        col_queue=collections.deque()
        visited = set() 

        row_queue.append(0)
        col_queue.append(0)
        visited.add((0,0))

        length = 1 # <- the example counts the START cell as +=1 
        while len(row_queue) > 0: # or col_queue
            for i in range(len(row_queue)):
                r = row_queue.popleft()
                c = col_queue.popleft()
                if r==ROWS-1 and c==COLS-1:
                    return length 
                for i in range(8): # 8-directional
                    dr = row_dirs[i]
                    dc = col_dirs[i]
                    if (r+dr<0 or c+dc<0 or r+dr==ROWS or c+dc==COLS) or ((r+dr,c+dc) in visited) or (grid[r+dr][c+dc]==1):
                        continue 
                    row_queue.append(r+dr)
                    col_queue.append(c+dc)
                    visited.add((r+dr,c+dc))
            length+=1 
        return -1
