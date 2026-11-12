class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        def dfs(grid, r, c, colorToFill):
            #BASE CASE 1: Invalid if out-of-bounds or position is == 0 or 2 
            if (r < 0 or c < 0 or r==ROWS or c==COLS) or (image[r][c]==color or image[r][c]!=colorToFill):
                return grid
            
            grid[r][c] = color 
            dfs(grid, r+1, c, colorToFill)
            dfs(grid, r-1, c, colorToFill)
            dfs(grid, r, c+1, colorToFill)
            dfs(grid, r, c-1, colorToFill)
            return grid

        selectedColor = image[sr][sc]
        return dfs(image, sr, sc, selectedColor)

#The moment we call `floodFill`, there is only ONE color we are searching to fill with a replacement color. 