'''
This file holds all the relavant scripts for the FLoc App under Agua Clara
    Functions:
    Examples:
    Dependencies:
                                                                Cheers,
                                                                -Floc App Team
'''

# Start of Imports
import glob
# End of Imports

'''
Purpose:
    - The applyTo function will open the folder at the provided path and then
    apply a given function to all the photos in the folder
Parameters:
    - Path to folder ex: "usr/aguaclara/documents/images"
    - Note the images should be .jpg
    - Function f
Returns:
    - Whatever f would have outputted
Raises:
    -
'''
def applyTo(path, fcn):
    for file in glob.glob(os.path.join(path, "*.jpg")):
        fcn(file)

'''
Purpose:
    - Noise Reduction
Parameters:
Returns:
Raises:
'''
