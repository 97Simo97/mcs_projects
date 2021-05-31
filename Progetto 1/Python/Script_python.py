# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:44:51 2021

@author: Simone Ritucci, Kevin Manella
"""

import numpy as np
import scipy.io
import scipy.sparse
import scipy.sparse.linalg
import sys
import time
import os
import psutil

def matrix_solver(directory_sparse_matrix):
    #matrix load
    a = scipy.io.mmread(directory_sparse_matrix)
    #fill zero matrix
    xe = np.ones(a.shape[0])
    
    #product column-row matrix
    b = a.dot(xe)

    start_time = time.time()
    #solve matrix
    x = scipy.sparse.linalg.spsolve(a, b, use_umfpack=True)
    elapsed_time = time.time() - start_time

    #calculate error
    error = np.linalg.norm(x - xe) / np.linalg.norm(xe)
    
    #calculate memory
    process = psutil.Process(os.getpid())
 
    
    print("Matrice: " , directory_sparse_matrix)
    print("Dimensione: ", a.shape[0])
    print("Tempo: ", elapsed_time)
    print("Errore: ", error)
    print("Memoria: ", (process.memory_info().rss)/1e+6)


matrix_solver('ns3Da.mtx')
atrix_solver('TSC_OPF_1047.mtx')

