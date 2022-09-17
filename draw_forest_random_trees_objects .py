#####################################FUENTES###########################################################
## https://www.youtube.com/watch?v=-LsuiVGO-88                                                       ##
## Draw a Forest of Random Tree Objects with Python OpenCV - Classes and OOP Practice for Beginners  ##
## https://github.com/MariyaSha/OpenCV_DrawImages/blob/main/completeCode_OpenCVForest.ipynb          ##
#######################################################################################################
# class X():
#     class_attribute_1 = 0
#     class_attritube_2 = 0
#     class_attritube_3 = 0
    
#     def __init__(self, instance_attribute_1, instance_attribute_2): #constructor
#         self.instance_attribute_1 = instance_attribute_1
#         self.instance_attribute_2 = instance_attribute_2
        
#     def metodo(self):
#         print("...")
        
#     def __str__(self): #representacion, ejemplo: tipo de objeto
#         return f"The values are: {self.instance_attribute_1}"
#         self.instance_attribute_2 = instance_attribute_2
    
#     def __len__(self): #representacion, ejemplo: tipo de objeto
#         return len(self.instance_attribute_1)
    
#     def __getitem__(self, pos):
#         return self.instance_attribute_1[pos]    
    
#     def __setitem__(self, pos, value):
#         self.instance_attribute_1[pos] = value
        
#     def __iter__(self):
#         for pos in range(0, len(self.instance_attribute_1)):
#             yield f"Value[{pos}]: {self.instance_attribute_1[pos]}"
    
        
#     def metodo(self):
#         print("...")
            

# x67i = X([5, 12], 0)
# print(x67i)
# len(x67i)
# for vec in x67i:
#     print(vec)
######################################################################################################
######################################################################################################
import numpy as np
import cv2 as cv
import random

#general parameters
width = 900
height = 600
n_tress = 30
ground_level = height -100

#colours
green, light_gree, brown = (40, 185, 40), (25, 220, 0), (30,65, 155)

#blank image
bg = np.zeros((height, width, 3), dtype = np.uint8)

#draw background
cv.rectangle(bg, (width, 0), (0, ground_level), (225, 225, 95), -1)
cv.rectangle(bg, (width, ground_level), (0, height), green, -1)
################
class Tree(object):
    def __init__(self, image, location):
        self.img = image
        self.loc =location
        self.ht = 300
        self.radius = 100
    def draw(self):
        #trunk=> cv.line(image, start_point, end_point, color, thickness) 
        cv.line(self.img, (self.loc, ground_level), (self.loc, ground_level-self.ht), brown, 40)
        cv.line(self.img, (self.loc, ground_level-self.ht + 150), (self.loc-90, ground_level-self.ht + self.radius-40), brown, 10)
        cv.line(self.img, (self.loc, ground_level-self.ht + 150), (self.loc+90, ground_level-self.ht + self.radius-40), brown, 10)
        #leafs=> cv.circle(image, center_coordinates, radius, color, thickness)
        cv.circle(self.img, (self.loc, ground_level-self.ht), self.radius, green, -1)
        cv.circle(self.img, (self.loc-90, ground_level-self.ht + self.radius-40), self.radius-40, green, -1)
        cv.circle(self.img, (self.loc+90, ground_level-self.ht + self.radius-40), self.radius-40, green, -1)
        return self.img
        
    
################

#DISPLAY IMAGE
img = Tree(bg, 450).draw()
cv.imshow('forest of objects', bg)

cv.waitKey(0)
cv.destroyAllWindows()













