# -*- coding: utf-8 -*-
"""

Function to create a user defined array which outputs a user defined number of 
vertical white stripes on an initial array of black and output image.

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



def vertical_image(rows, cols, num_stripes):
    
   stripe_count = num_stripes
   stripe_interval = int(cols/num_stripes)
   #image_array = []
   image_array = np.zeros((rows,cols))
   col_start = 0
   col_end = stripe_interval
   
   while stripe_count >= 2:

       if stripe_count %2:
           stripe_count -=1
       else: 
           image_array[:,col_start:col_end] = 255
           stripe_count -= 1
           
       #print(stripe_count)
       col_start = col_end+1
       col_end = col_end + stripe_interval
       
   return image_array


def input_data():
     array_input = input("enter number of height and width of array (seperated by ,):......")
     array_input = array_input.split(',')
     rows = int(array_input[0])
     cols = int(array_input[1])
     
     num_stripes = int(input("insert a number of stripes:......"))
     
     return rows, cols, num_stripes

           
def main():
    
    rows, cols, num_stripes = input_data()
    image_array = vertical_image(rows, cols, num_stripes)
    image_out = Image.fromarray(image_array)
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