# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:11:59 2021

@author: Ritucci Simone, 813473
"""

import Script1 as s
import numpy as np                   #Per gli array n-dimensionali
import time
import matplotlib.pylab as plot
from matplotlib import pyplot

"""
main()
"""
def main():
    values_of_dimension = [50,100,150,200,250,300,350,400,
                           450,500,550,600,650,700,750,800]   
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
    #print(scipy_time)
    #print(my_dct2_time)  
  
    plot.title("Comparison")
    plot.xlabel("Dimension")
    plot.ylabel("Time")    
    plot.plot(values_of_dimension, scipy_time, 
              label = 'Scipy', color = "pink")
    plot.plot(values_of_dimension, my_dct2_time, 
              label = 'My_dct2', color = "green")
    plot.legend()
    plot.xlim(values_of_dimension[0], 
              values_of_dimension[len(values_of_dimension)-1])
    plot.ylim(0, my_dct2_time[len(my_dct2_time) - 1])     
    pyplot.savefig('Comparison.png', bbox_inches='tight',  dpi=200)
    
    s.first_test()
    s.second_test()
    
if __name__=="__main__":
    main()
    