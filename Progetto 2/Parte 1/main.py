# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:11:59 2021

@author: Ritucci Simone, 813473
"""

import Script1 as s
import numpy as np                   #Per gli array n-dimensionali
import time

"""
main()
"""
def main():
    values_of_dimension = [200,400,600,800,1000,
                           1200,1400,1600,1800,2000]   
    scipy_time = []
    my_dct2_time = []    
    
    for x in values_of_dimension:
        matrix = np.random.randint(256, size=(x,x))   
        
        time1 = time.time()
        s.dct2_scipy(matrix)
        time2 = time.time()
        scipy_time.append(time2 - time1)

        time3 = time.time()
        s.my_dct2(matrix)
        time4 = time.time()        
        my_dct2_time.append(time4-time3)
        
    #TEMPI in console
    print(scipy_time)
    print(my_dct2_time)  
    
    s.first_test()
    s.second_test()
  
    
if __name__=="__main__":
    main()
    