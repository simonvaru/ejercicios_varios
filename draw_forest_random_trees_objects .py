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

######################
##general parameters##
######################
width = 900
height = 600
n_tress = 30
ground_level = height -100

###########
##colours##
###########
green, light_green, brown = (40, 185, 40), (25, 220, 0), (30,65, 155)

###############
##blank image##
###############
bg = np.zeros((height, width, 3), dtype = np.uint8)

############
##draw sky##
############
cv.rectangle(bg, (width, 0), (0, ground_level), (225, 225, 95), -1)

################
class Tree(object):
    def __init__(self, image, location):
        self.img = image
        self.loc =location
        self.ht = 300
        self.radius = 50
        self.scale = 2
    def draw(self):
        small_radius = self.radius*self.scale-20*self.scale
        #leafs=> cv.circle(image, center_coordinates, radius, color, thickness)
        cv.circle(self.img, (self.loc, ground_level-self.ht), self.radius*self.scale, green, -1)
        cv.circle(self.img, (self.loc-45*self.scale, ground_level-self.ht + small_radius), small_radius, green, -1)
        cv.circle(self.img, (self.loc+45*self.scale, ground_level-self.ht + small_radius), small_radius, green, -1)
        #trunk=> cv.line(image, start_point, end_point, color, thickness) 
        cv.line(self.img, (self.loc, ground_level), (self.loc, ground_level-self.ht), brown, 20*self.scale)
        cv.line(self.img, (self.loc, ground_level-self.ht + 75*self.scale), (self.loc-45*self.scale, ground_level-self.ht + small_radius), brown, 5*self.scale)
        cv.line(self.img, (self.loc, ground_level-self.ht + 75*self.scale), (self.loc+45*self.scale, ground_level-self.ht + small_radius), brown, 5*self.scale)
        #leafs-shadows
        cv.circle(self.img, (self.loc, ground_level-self.ht), self.radius*self.scale-10*self.scale, light_green, -1)
        cv.circle(self.img, (self.loc-45*self.scale, ground_level-self.ht + small_radius), small_radius-10*self.scale, light_green, -1)
        cv.circle(self.img, (self.loc+45*self.scale, ground_level-self.ht + small_radius), small_radius-10*self.scale, light_green, -1)
        return self.img
    
    
    
################        
    

#################
##display image##
#################
img = Tree(bg, 450).draw()

###############
##draw ground##
###############
cv.rectangle(bg, (width, ground_level), (0, height), green, -1)

##############################
##show in individual windows##
##############################
cv.imshow('forest of objects', bg)
cv.waitKey(0)
cv.destroyAllWindows()













