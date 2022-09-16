# from ast import increment_lineno
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as pltcls

# #matplotlib inline

# titanic_df = pd.read_excel('titanic3.xls', 'titanic3', index_col = None, na_values = ['NA'])
# titanic_df.head()

# from pathlib import Path
# import pandas as pd
# E:\pythondoc\.vscode\titanic3.xls
# .vscode\titanic3.xls


# data_path = Path(r"E:\pythondoc\.vscode\texto_prueba.txt")
# file_to_open = open(data_path)

# print("TIPO: ", type(file_to_open))
# print("CONTENIDO:\n", file_to_open.read(), "\n"*3)



# data_path_2 = Path(r"E:\pythondoc\ejercicios_varios\titanic3.xlsx")
# # file_to_open_2 = open(data_path_2)

# # print("TIPO: ", type(file_to_open_2))
# dataframe_1 = pd.read_excel(data_path_2)
# print(dataframe_1)
# print("CONTENIDO:\n", file_to_open_2.read(), "\n"*3)
# E:\pythondoc\ejercicios_varios\titanic3.xlsx


# archivo_abierto_2 = open("E:\pythondoc\.vscode\texto_prueba.txt")
# print("TIPO: ", type(archivo_abierto_2))
# print("CONTENIDO.", archivo_abierto_2.read())

#==============================================================================================

# print("\n"*1)
# cadena1 = "soY la pRimer cadena"
# print(cadena1)
# print("\n"*2)

# cadena1_en_mayusculas = cadena1.upper()
# print(cadena1_en_mayusculas)
# print("\n"*3)

# cadena1_titleada = cadena1.title()
# print(cadena1_titleada)
# print("\n"*4)

# c = cadena1.count("a")
# print(c)
# print("\n"*5)

# c = cadena1.count("a", 7, 16)
# print(c)
# print("\n"*6)

# d = len(cadena1)
# e = cadena1.rfind("ade")
# f = cadena1.find("adE")
# print(e)
# # print(f)
# c = cadena1.count("ade", -1, 20)
# c1 = cadena1.count("a", -1, d)
# c2 = cadena1.count("ade", e, d)
# print(c)
# print(c1)
# print(c2, "\n"*3)

#==============================================================================================

# cadena_2 = "segunda cadena al rescate"
# cadena_2_spliteada = cadena_2.split(" ")
# print(cadena_2_spliteada)
# print(cadena_2_spliteada[2])
# cadena_2_spliteada.append(40)
# print(cadena_2_spliteada)
# cadena_2_spliteada.remove(40)
# print(cadena_2_spliteada)

#==============================================================================================

# cadena_2 = {23, 2, 67, 99, 11, 3, 845, 7, "Hola"}

# print(cadena_2)
# cadena_2.pop()
# print(cadena_2)
# cadena_2.pop()
# print(cadena_2)
# cadena_2.pop()
# print(cadena_2)
# cadena_2.pop()
# print(cadena_2)
# cadena_2.pop()
# print(cadena_2)
# cadena_2.pop()
# print(cadena_2)
# cadena_2.pop()
# print(cadena_2)
# cadena_2.update({"avion", 47, "A"})
# print(cadena_2)
# cadena_2.discard("Hola")
# print(cadena_2)

# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)

#==============================================================================================

# auto ={
#     "motor": "v12",
#     "kilometraje": 130000,
#     "vidrios": (1, "blindados")
# }
# x = auto.values()
# print(x)
# y = auto.keys()
# print(y)
# for key, value in auto.items():
#     print(f"Para la key {key} el valor es {value}.")
   
# print("\n"*2)    

# auto["vidrios"] = (5, "blindados")
# auto["color"] = "rojo"
# print(x)
# print(y)

# for key, value in auto.items():
#     print(f"Para la key {key} el valor es {value}.")

















#=================================PANDA+EXCEL+EDITAR+FUNCIONAOK=================================
#  from pathlib import Path
# import pandas as pd


# data_path = Path(r"E:\pythondoc\.vscode\texto_prueba.txt")
# file_to_open = open(data_path)

# print("TIPO: ", type(file_to_open))
# print("CONTENIDO:\n", file_to_open.read(), "\n"*3)



# data_path_2 = Path(r"E:\pythondoc\ejercicios_varios\titanic3.xlsx")

# dataframe_1 = pd.read_excel(data_path_2)
# print(dataframe_1)

#=======================================greyscale+BGR+office_building=============================
# import numpy as np
# from PIL import Image


# width, height = 800, 800
# cv2.imwrite("325a.png", img) 
# location = 0
# shade = 0
# n_shades = 255
# for i in range(n_shades):
#     img[0:height, location: location+width//n_shades, 1:2:1] = shade
#     location += width//n_shades
#     shade += 255//n_shades

# # cv2.imwrite("325a.png", img)
# #=======================================
# import numpy as np
# from PIL import Image


# width, height = 600, 800


# img = np.zeros((height, width, 3), dtype = np.uint8)
# img[:] =(35, 29, 43)
# img[int(height*0.85):height, 0: width] = (35, 55, 43)

# img[int(height*0.1):int(height*0.9), int(width*0.2):int(width*0.8)] = (94, 101, 107)

# for row in range(6):
#     for column in range(5):
#         if np.random.randint(0,8) == 5:
#             windows_colour = (240, 230, 140)
#         else:
#             windows_colour = (28, 23, 35)
#         img[
#         int(height*0.1 +100*row+20):int(height*0.1 +100*row+60 +20),
#         int(width*0.2+75*column+15):int(width*0.2+75*column+30+15)
#         ] = windows_colour

# Image.fromarray(img).save("my_image.png")

# #=======================================
# import numpy as np
# from PIL import Image

# width, height = 600, 800
# # create blank image
# img = np.zeros((height, width, 3), dtype=np.uint8)

# # draw background
# img[:] = (35, 29, 43)
# img[int(height*0.85):height, 0:width] = (35, 55, 43)

# # draw building
# img[int(height*0.1):int(height*0.9), int(width*0.2):int(width*0.8)] = (94, 101, 107)

# # office windows logic
# for row in range(6):
#     for column in range(5):
#         # select random window colours
#         if np.random.randint(0,8) == 5:
#             window_colour = (240, 230, 140)
#         else:
#             window_colour = (28, 23, 35)
#         # draw windows
#         img[
#             int(height*0.1 + 100*row + 20):int(height*0.1 + 100*row + 60 + 20),
#             int(width*0.2 + 75*column + 15): int(width*0.2 + 75*column + 30 + 15)
#             ] = window_colour

# # save image
# Image.fromarray(img).save("my_img.png")
#=======================================

# lista = [2, 5, 7, "hurra"]
# x = len(lista)
# print(x)
# print(lista)
# for i in range(0,x):
#     print(lista[i])
# else:
#     y = lista.pop(i)
#     print(y)
#     print("finish")    
# print(lista)
#=======================================      
# while (True):
#     try:
#         n = float(input("Introduce numero: "))
#         m = 4
#         print("{}/{} = {}".format(n, m, n/m))
#         break
#     except:
#         print("Algo salio mal.")
#     else:
#         print("Todo salio bien.")
#         break
#     finally:
#         print("despues de finally.") 
# #=======================================             
# def dividir(a, b):
#     return a/b

# print(dividir(8, 3))
# #=======================================
# try:
#     n = float(input("Introduce un numero: "))
#     print(5/n)
# except Exception as e:
#     print("Ha ocurrido un error=>", type(e))
# print("Tipo: ", type(1).__name__)
# print("Tipo: ", type(3.14).__name__)
# print("Tipo: ", type("y").__name__)
# print("Tipo: ", type(4 + 6j).__name__)
# print("Tipo: ", type(0).__name__)
# #=======================================


# def funcion_x():
#     return None

# print(funcion_x)

# while(True):
#     try:
#         n = float(input("Introduce un numero divisor: "))
#         # math.sqrt(n)
#         print(5/n)
#     except TypeError:
#         print("No se puede dividir el numero entre una cadena.")
#     except ValueError:
#         print("Debes introducir una cadena que sea un numero.")
#     except ZeroDivisionError:
#         print("No se puede dividor por cero.")
#         print(fx)  
#     except Exception as e:
#         print("error no previsto: ", type(e).__name__)            
# #========================Graphics=============



# from PIL import Image, ImageChops, ImageFilter
# from pathlib import Path
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# data_path_x = Path(r"E:\pythondoc\ejercicios_varios\x.png")
# mg = mpimg.imread(data_path_x)
# plt.imshow(img)
# plt.show()


# data_path_x = Path(r"E:\pythondoc\ejercicios_varios\x.png")
# data_path_o = Path(r"E:\pythondoc\ejercicios_varios\o.png")
# x = Image.open(data_path_x)
# o = Image.open(data_path_o)
# # x.show()#muestra en pantalla grafico
# # o.show()#muestra en pantalla grafico

# print("Size  o: {}\nSize x: {}\nColour mode o: {}\nColour mode x: {}".format(o.size, x.size, o.mode, x.mode))

# plt.subplot(121), plt.imshow(x)
# plt.axis("off")
# plt.subplot(122), plt.imshow(o)
# plt.axis("off")

# merged = ImageChops.multiply(x, o)
# # merged.show()#muestra en pantalla imagenes juntas
# # add = ImageChops.add(x, 0)
# greyscale = merged.convert("L")
# greyscale.show()
# #======================Maths=============
# import math
# import math as m
# from math import sqrt, pow
# import math as m

# print("3", end = "")
# print("2", end="")
# print(m.pi) 
# print(m.sqrt(m.pi))
# print(m.floor(2.5))
# print(m.ceil(2.5))
# print(int(2.5))
# print(m.pow(3,2), end="  ")
# print(m.pow(3,3), end = "    ")
# print(m.pow(3,4), end =" ")
# print("\n"*3)
# print(m.pow(9,1/2))
# print(m.pow(9,-2), end="  =?  ")
# print(1/m.pow(9,2))


# #======================Panda=============
weight = 73.5
height = 1.69
bmi =weight/(height**2)
print(bmi)





