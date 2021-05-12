# -*- coding: utf-8 -*-
"""

Function to accept an array of random floats within a user defined amplitude 
range (e.g -1024 to 1024 or 0 to 16384), and normalise between 0 and 1.

Greyscale image of array is output for visual representation 

@author: michael@eilonal.uk

versions of libraries
---------------------
numpy          1.20.3
Pillow         8.2.0


Spyder Editor


"""

import numpy as np
from PIL import Image



def normalise_array(array_in):
    
    # normalise array
    min = np.amin(array_in)
    max = np.amax(array_in)
    rng = max - min
    
    array_norm = (array_in - min) / rng
    
    
    image = Image.fromarray(np.uint8(array_norm*255))
    
    return image



def input_data():
     array_input = input("enter number of height and width of array (seperated by ,):......")
     array_input = array_input.split(',')
     rows = int(array_input[0])
     cols = int(array_input[1])
     
     min_float = float(input("insert a minimum for array values:......"))
     max_float = float(input("insert a maximum for array values:......"))
     
     array_in = np.random.rand(rows, cols)
     
     if np.amin(array_in) < min_float or np.amax(array_in) > max_float:
         print('Value error: input array value is outside correct range')
     
     return array_in


           
def main():
    
    array_in = input_data() 
    image_out = normalise_array(array_in)
    image_out.show()     

if __name__ == '__main__':   
    
    main()
    
    
    
#------------------------------------------------------------
__author__ = "Michael Robinson"
__copyright__ = "Copyright 2021, M Robinson"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "M Robinson"
__status__ = "Prototype"