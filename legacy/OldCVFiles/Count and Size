

# Written by Richard Yu (ry275@cornell.edu)

import cv2


# Returns: A 2-dimensional list/grid that contains value True or False, which denotes whether a coordinate is a 
# "near-white" pixel (R >= 225, G >= 225, B >= 225) or not
# Requires: an RGB 3-dimensional list/picture 
def whitePixels(grid):
    res = [[True for y in range(len(grid[0]))] for x in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            curPixel = grid[i][j]
            for rgb in curPixel:
                 if rgb < 225:
                        res[i][j] = False
                        break
    return res



import sys

# Returns: the count of non-zero (black) pixels for an inputted picture/3-dimensional list
# Requires: a 3-dimensinoal list/picture
def nonBlackPixels(img):
    return cv2.countNonZero(img)



# Returns: scales down img's [i],[j] dimensions by a factor of 5, effectively shrinking the image to 1/25 its original size
# Requires: a 3-dimensional list/picture
def shrink5x(img):
    shrunk = cv2.resize(img,None,fx=.2, fy=.2, interpolation = cv2.INTER_CUBIC)
    return shrunk



# Returns: a 5-tuple, containing the count of "near-white" pixel (R >= 225, G >= 225, B >= 225) islands, a 
# list containing the counts of near-white pixels for each individual island, the total count of near-white pixels, 
# the total count of non-black pixels, and a string explaining if there is a noticeable difference between the 
# sum of individual near-white pixel counts and the total count of non-black pixels.
# Requires: an RGB 3-dimensional list/picture 
def count_and_size_flocs(img):
        
        # Increases the recursive call stack limit to 100,000 to ensure 
        # that the method does not give a "recursion/stack overflow" error
        sys.setrecursionlimit(100000)
        
        # Shrinks img to reduce the number of pixels this method has to iterate over
        shrunk = shrink5x(img)
        shrunk = whitePixels(shrunk)
        islands = 0
        
        i_flocBounds = []
        j_flocBounds = []
        
        for i in range(len(shrunk)):  
            for j in range(len(shrunk[i])):
                if shrunk[i][j] == True:
                    iCoords = [i]
                    jCoords = [j]
                    part_of_island(i, j, shrunk, iCoords, jCoords)
                    i_flocBounds_raw = ([min(iCoords) * 5 - 5,max(iCoords) * 5 + 5])
                    j_flocBounds_raw = ([min(jCoords) * 5 - 5, max(jCoords) * 5 + 5])
                    if (i_flocBounds_raw[0] <= 0):
                        i_flocBounds_raw[0] = 0
                    if (i_flocBounds_raw[1] >= len(img) - 1):
                        i_flocBounds_raw[1] = len(img) - 1
                    if (j_flocBounds_raw[0] <= 0):
                        j_flocBounds_raw[0] = 0
                    if (j_flocBounds_raw[1] >= len(img[0]) - 1):
                        j_flocBounds_raw[1] = len(img[0]) - 1
                    i_flocBounds.append(i_flocBounds_raw)
                    j_flocBounds.append(j_flocBounds_raw)
                    islands += 1
        
        print(i_flocBounds, j_flocBounds)
        flocAreas = whitePixelAreas(i_flocBounds, j_flocBounds, img)
        nonBlacks = nonBlackPixels(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
        flocAreasTotal = sum(flocAreas)
        description = ""
        if (abs(flocAreasTotal - nonBlacks) >= (nonBlacks/5)):
            description = "There is GREATER THAN a 20% discrepancy between the sum of individual near-white pixel counts and the total count of non-black pixels! There are many non-black AND non-near-white pixels!"
        else:
            description = "There is LESS THAN a 20% discrepancy between the sum of individual near-white pixel counts and the total count of non-black pixels."
        return islands, flocAreas, nonBlacks, description



# Returns: nothing, but sets all adjacent near-white pixels to black pixels and appends the coordinates of adjacent 
# near-white pixels to a list of [i] coordinates and a list of [j] coordinates
# Requires: a single [i][j] coordinate of a near-white pixel for a 3-dimensional list/picture, 
# a T/F 2-dimensional list/grid, a list of [i] cooridinates for adjacent near-white pixels, 
# and a list of [j] coodinates for adjacent near-white pixels.
def part_of_island(i, j, grid, iCoords, jCoords):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[i]) or (grid[i][j] == False):
            return
        else:
            grid[i][j] = False
            iCoords.append(i)
            jCoords.append(j)
        part_of_island(i,j+1,grid, iCoords, jCoords)
        part_of_island(i,j-1,grid, iCoords, jCoords)
        part_of_island(i+1,j,grid, iCoords, jCoords)
        part_of_island(i-1,j,grid, iCoords, jCoords)
        part_of_island(i+1,j+1,grid, iCoords, jCoords)
        part_of_island(i+1,j-1,grid, iCoords, jCoords)
        part_of_island(i-1,j+1,grid, iCoords, jCoords)
        part_of_island(i-1,j-1,grid, iCoords, jCoords)



# Returns: a 2-dimensional list that is a "subgrid" of the inputted 2-dimensional list
# Requires: a min [j] and max [j] coordinate, a min [i] and max [i] coordinate, and a 2-dimensional list (a grid)
def getsubgrid(j1, i1, j2, i2, grid):
    return [item[j1:j2] for item in grid[i1:i2]]



# Returns: a list containing the counts of near-white pixels for every "near-white pixel island" in a picture
# Requires: a list of tuples containing the [i] coordinate bounds and a list of tuples containing 
# the [j] coordinate bounds that locates each near-white pixel island for an inputted RGB 3-dimensional list/picture.
def whitePixelAreas(i_flocBounds, j_flocBounds, img):
    subgrids = []
    floc = 0
    for flocBound in i_flocBounds:
        i_Bounds = i_flocBounds[floc]
        j_Bounds = j_flocBounds[floc]
        subgrids.append(getsubgrid(j_Bounds[0], i_Bounds[0], j_Bounds[1], i_Bounds[1],img))
        floc = floc+1
   
    whitePixelGrids = []
    for subgrid in subgrids:
        whitePixelGrids.append(whitePixels(subgrid))
    
    flocAreas = []
    for img in whitePixelGrids:
        pixels = 0
        for i in range(len(img)):  
            for j in range(len(img[i])):
                if img[i][j] == True:
                    pixels = pixels + 1
        flocAreas.append(pixels)
    return flocAreas



# Example usage
img = cv2.imread("pureblack.jpg")
count_and_size_flocs(img)



