class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1 
        # Init your variables Data Science style 
        ROWS,COLS = len(grid), len(grid[0])
        neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set() 
        queue = collections.deque() 
        queue.append([0,0])

        length = 0 
        while len(queue) > 0:
            for i in range(len(queue)):
                element = queue.popleft()
                r,c = element[0],element[1]
                if ((r==ROWS-1) and (c==COLS-1)):
                    return length
                for dr,dc in neighbors:
                    if (r+dr<0 or c+dc<0 or r+dr==ROWS or c+dc==COLS) or ((r+dr,c+dc) in visited) or (grid[r+dr][c+dc]==1):
                        continue 
                    #else:
                    visited.add((r+dr, c+dc))
                    queue.append([r+dr, c+dc])
            #each breadth, for each direction, will have length+=1 
            length+=1 
        return -1 
                
        