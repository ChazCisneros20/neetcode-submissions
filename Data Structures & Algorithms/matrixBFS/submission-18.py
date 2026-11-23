class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[len(grid)-1][len(grid[0])-1]==1:
            return -1 
        ROWS,COLS = len(grid), len(grid[0])
        #up/down/left/right in that order
        row_dirs = [-1, 1, 0, 0]
        col_dirs = [0, 0, -1, 1]
        visited = set() 
        row_queue = collections.deque()
        col_queue = collections.deque() 
        row_queue.append(0)
        col_queue.append(0)
        visited.add((0,0))

        length = 0  # <- MUST BE length=1 b/c the first top-left-most node (0,0) was enqueued and added to visited HashSet()
        while len(row_queue)>0:
            for i in range(len(row_queue)):
                r = row_queue.popleft() 
                c = col_queue.popleft() 
                if r==ROWS-1 and c==COLS-1:
                    return length
                for i in range(4): # for 4 directions up/down/left/right
                    dr = row_dirs[i]
                    dc = col_dirs[i]
                    if (r+dr<0 or c+dc<0 or r+dr==ROWS or c+dc==COLS) or (grid[r+dr][c+dc]==1) or ((r+dr,c+dc) in visited):
                        continue
                    # else if the r+dr,c+dc is a valid [0] cell 
                    visited.add((r+dr, c+dc))
                    row_queue.append(r+dr)
                    col_queue.append(c+dc)
            length+=1 # each breadth of noes is simultaneously* traversing by one cell path-length
        return -1 

        