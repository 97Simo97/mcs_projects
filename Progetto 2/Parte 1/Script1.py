"""
Created on Mon Jan 11 12:10:18 2021

@author: Ritucci Simone, 813473
"""

import numpy as np                   #Per gli array n-dimensionali
from scipy.fftpack import dct        #Per la DCT2 del modulo scipy.fftpack
import math

"""
dct2_scipy(old_matrix)
funzione che esegue la dct2 implementata in scipy.fftpack
prendendo in input matrici bidimensionali
"""
def dct2_scipy(old_matrix):

    #DCT1 su righe 
    new_matrix = np.transpose(old_matrix)
    new_matrix = dct(old_matrix, type = 2, norm = 'ortho')
    
    #DCT1 su colonne     
    new_matrix = np.transpose(new_matrix)
    new_matrix = dct(new_matrix, type = 2, norm = 'ortho')
                
    return new_matrix

"""
my_dct2(old_matrix)
funzione che esegue la dct2, per righe e per colonne,
prendendo in input una matrice bidimensionale
"""
def my_dct2(old_matrix):
    
    #DCT1 su righe 
    new_matrix = np.transpose(old_matrix)
    new_matrix = my_dct1(new_matrix)
    
    #DCT1 su colonne     
    new_matrix = np.transpose(new_matrix)
    new_matrix = my_dct1(new_matrix)
                
    return new_matrix
        
"""
my_dct1(x)
funzione che esegue la dct1 prendendo in input una lista di interi int
"""
def my_dct1(old):
    dct1 = []   
    
    for k in range(0, len(old)):
        sum = 0
        if k == 0:
            coeff = math.sqrt(1 / len(old))
        else:
            coeff = math.sqrt(2 / len(old)) 
        for j in range(0, len(old)):
            var_dct = (old[j] * math.cos(math.pi * k * (2 * j + 1) / (2 * len(old)))) 
            sum += var_dct          
        dct1.append(coeff * sum)
    
    return dct1

"""
first_test()
test che controlla che venga effettuato lo scaling corretto 
visto a lezione per la dct1
"""
def first_test():
    vector = [231, 32, 233, 161, 24, 71, 140, 245]
     
    test_dct1_1 = dct(vector, type = 2, norm='ortho')
    print("Test 1 dimensione")
    print("Scipy: ")
    
    for x in test_dct1_1:
        print("{:.2e}".format(x))
    
    test_dct1_2 = my_dct1(vector)
    print("********************")
    print("My_dct1: ")

    for y in test_dct1_2:
        print("{:.2e}".format(y))
        
    print("Test OK")
      
"""
second_test()
test che controlla che venga effettuato lo scaling corretto 
visto a lezione per la dct2
"""
def second_test():
    array_prova = [[231, 32, 233, 161, 24, 71, 140, 245], 
            [247, 40, 248, 245, 124, 204, 36, 107],
            [234, 202, 245, 167, 9, 217, 239, 173],
            [193, 190, 100, 167, 43, 180, 8, 70],
            [11, 24, 210, 177, 81, 243, 8, 112],
            [97, 195, 203, 47, 125, 114, 165, 181],
            [193, 70, 174, 167, 41, 30, 127, 245],
            [87, 149, 57, 192, 65, 129, 178, 228]]
    
    test_dct2_1 = dct2_scipy(array_prova)
    print("************************************************************")
    print("Test 2 dimensioni")
    print("Scipy: ")   
    for x in range(0,8):
        for y in range(0,8):
            print("{:.2e}".format(test_dct2_1[x][y]))
    print("********************")
    print("My_dct2:")  
    test_dct2_2 =my_dct2(array_prova)
    for k in range(0,8):
        for j in range(0,8):
            print("{:.2e}".format(test_dct2_2[k][j]))     
    print("Test OK")    

