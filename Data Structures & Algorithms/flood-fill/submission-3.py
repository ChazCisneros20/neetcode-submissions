class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        ROWS,COLS = len(image), len(image[0])
        row_dirs, col_dirs = [-1,1,0,0], [0,0,-1,1]
        if color==start_color:
            return image 
        # no visted() HashSet() b/c we just check if up/down/left/right neighboring pixels are == start_color
        def dfs(grid, r, c):
            if (r<0 or c<0 or r==ROWS or c==COLS) or (grid[r][c]!=start_color):
                return 
            grid[r][c]=color 
            for i in range(4):
                dfs(grid, r+row_dirs[i], c+col_dirs[i])
            
        dfs(image, sr, sc)
        return image

            
