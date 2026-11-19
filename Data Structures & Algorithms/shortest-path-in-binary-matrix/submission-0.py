class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        if grid[len(grid)-1][len(grid[0])-1]==1:
            return -1 
        ROWS,COLS=len(grid),len(grid[0])
        row_queue = collections.deque()
        col_queue = collections.deque()
        visited = set()  
        # up/down/left/right , top-right/bottom-left/top-left/bottom-right
        row_dirs = [-1, 1, 0, 0, -1, 1, -1, 1]
        col_dirs = [0, 0, -1, 1, 1, -1, -1, 1]
        visited.add((0,0))
        row_queue.append(0)
        col_queue.append(0)
        length = 1
        while (len(row_queue) > 0):   # or col_queue
            for i in range(len(row_queue)):
                r = row_queue.popleft()
                c = col_queue.popleft()
                if r==ROWS-1 and c==COLS-1:
                    return length  
                for i in range(8):    # for 8-directions 
                    dr = row_dirs[i]
                    dc = col_dirs[i]
                    if (r+dr<0 or c+dc<0 or r+dr==ROWS or c+dc==COLS) or ((r+dr,c+dc) in visited) or (grid[r+dr][c+dc]==1):
                        continue 
                    #else:
                    row_queue.append(r+dr)
                    col_queue.append(c+dc)
                    visited.add((r+dr, c+dc))
            length+=1
        return -1 