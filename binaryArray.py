# -*- coding: utf-8 -*-
"""

A method to create a "false" binary array and convert a section of it to "true"
Plot output to visualise 


@author: michael@eilonal.uk

versions of libraries
---------------------
numpy          1.20.3
Pillow         8.2.0

Spyder Editor


"""

import numpy as np
from PIL import Image

class binaryArray:
    def __init__(self, rows, cols, top_left, bottom_right):
        self.rows = rows
        self.cols = cols
        self.x1 = top_left[0]
        self.x2 = bottom_right[0]
        self.y1 = top_left[1]
        self.y2 = bottom_right[1]
        
    def image_array(self):
        array = np.zeros((self.rows, self.cols), dtype='bool')
        array[self.x1:self.x2,self.y1:self.y2] = True
        #print('self.....',self.x1, self.x2, self.y1, self.y2)
        #print(type(self.x1))
        
        # tests of input
        error_out = []
        if self.x1 < 0 or self.x2  < 0  or self.y1  < 0 or self.y2 < 0:
            error_out = 'Value Error---- top left or bottom right cannot extend outside array'
            
        return array, error_out   


def input_data():
     array_input = input("enter number of rows and columns (seperated by ,):......")
     array_input = array_input.split(',')
     rows = int(array_input[0])
     cols = int(array_input[1])
     
     top_left_input = input("top left corner of box (seperated by ,):......")
     top_left_input = top_left_input.split(',')
     top_left = [int(top_left_input[0]), int(top_left_input[1])]
     
     bottom_right_input = input("bottom right corner of box (seperated by ,):......")
     bottom_right_input = bottom_right_input.split(',')
     bottom_right = [int(bottom_right_input[0]), int(bottom_right_input[1])]

     return rows, cols, top_left, bottom_right

           
def main():
    
     rows, cols, top_left, bottom_right = input_data()

     test_out = binaryArray(rows, cols, top_left, bottom_right)
     array_out, error_out = test_out.image_array()
     if error_out:
         print(error_out)
     image = Image.fromarray(array_out)
     image.show()
         

if __name__ == '__main__':   
    
    main()
    
    
    
#------------------------------------------------------------
__author__ = "Michael Robinson"
__copyright__ = "Copyright 2021, M Robinson"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "M Robinson"
__status__ = "Prototype"