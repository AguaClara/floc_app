
import cv2

# Returns: a 2-dimensional list that contains value True or False, denoting whether the coordinate is a white pixel or not
# Requires: a 3-dimensional list/picture 
def whitePixels(grid):
    res = [[True for y in range(len(grid[0]))] for x in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            curPixel = grid[i][j]
            for rgb in curPixel:
                 if rgb != 255:
                        res[i][j] = False
                        break
    return res

import sys

# Returns: the count of white pixel (RGB: [255,255,255]) islands. 
# Requires: a 3-dimensional list/picture 
def numWhiteIslands(img):
        
        # Increases the recursive call stack limit to 100,000 to ensure 
        # that the method does not give a "recursion/stack overflow" error
        sys.setrecursionlimit(100000)
        
        # Shrinks img to 1/25 its original size, reducing the number of pixels the method has to iterate over
        shrunk = cv2.resize(img,None,fx=.2, fy=.2, interpolation = cv2.INTER_CUBIC)
        shrunk = whitePixels(shrunk)
        islands = 0
        for i in range(len(shrunk)):  
            for j in range(len(shrunk[i])):
                if shrunk[i][j] == True:
                    islands += 1
                    part_of_island(i,j,shrunk)
        return islands

# Returns: nothing, but sets all connecting white pixels to black pixels.
# Requires: a [i][j] coordinate of a white pixel for a 3-dimensional list/picture 
def part_of_island(i, j,grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[i]) or (grid[i][j] == False):
            return
        else:
            grid[i][j] = False
        part_of_island(i,j+1,grid)
        part_of_island(i,j-1,grid)
        part_of_island(i+1,j,grid)
        part_of_island(i-1,j,grid)
        part_of_island(i+1,j+1,grid)
        part_of_island(i+1,j-1,grid)
        part_of_island(i-1,j+1,grid)
        part_of_island(i-1,j-1,grid)



# Example usage
img = cv2.imread("filtered_img.jpg")
numWhiteIslands(img)





