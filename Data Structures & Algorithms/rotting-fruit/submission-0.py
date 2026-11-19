class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        # using up/down/left/right
        row_dirs = [-1,1,0,0]
        col_dirs = [0,0,-1,1]
        ones    = set() 
        row_queue = collections.deque()
        col_queue = collections.deque() 


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    ones.add((i,j))
                if grid[i][j]==2:
                    row_queue.append(i)
                    col_queue.append(j)
        
        minutes = 0
        while len(row_queue) > 0: # or col_queue
            for i in range(len(row_queue)):
                r=row_queue.popleft()
                c=col_queue.popleft()
                for i in range(4):
                    dr=row_dirs[i]
                    dc=col_dirs[i]
                    if (r+dr<0 or c+dc<0 or r+dr==ROWS or c+dc==COLS) or (grid[r+dr][c+dc]!=1) :
                        continue
                    grid[r+dr][c+dc]=2
                    ones.remove((r+dr,c+dc)) 
                    row_queue.append(r+dr)
                    col_queue.append(c+dc)
            # only add a minute if there are remaining fresh fruits to "rot"
            # once the last fruit(s) are rotted, that happens in the middle of the algorithm
            # so we should NOT perform our usual minutes+=1 
            if len(row_queue) > 0:   
                minutes+=1
        if len(ones) > 0:
            return -1 
        return minutes

        
