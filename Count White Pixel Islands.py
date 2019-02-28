# Returns: the count of "white pixel [255,255,255]" islands. 
# Requires: a 3-dimensional list "grid" that contains only two values: [255,255,255] (white pixel) and [0,0,0] (black pixel)
def numIslands(grid):
        islands = 0
        for i in range(len(grid)):  
            for j in range(len(grid[0])):
                if (grid[i][j] == [255,255,255]).all():
                    islands += 1
                    part_of_island(i,j,grid)
        return islands

# Returns: nothing, but sets all connecting white pixels to black pixels.
# Requires: a (i,j) coordinate of a white pixel for a 3-dimensional list "grid" 
def part_of_island(i, j,grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or (grid[i][j] == [0,0,0]).all():
            return
        else:
            grid[i][j][0] = 0
            grid[i][j][1] = 0
            grid[i][j][2] = 0
        part_of_island(i,j+1,grid)
        part_of_island(i,j-1,grid)
        part_of_island(i+1,j,grid)
        part_of_island(i-1,j,grid)  

# Example use
img = cv2.imread("filtered_img.jpg")
numIslands(img)

