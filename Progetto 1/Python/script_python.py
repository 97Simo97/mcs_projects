import os
import time
import psutil
import numpy
import scipy
import scipy.io
import scipy.sparse
import scipy.sparse.linalg
import cvxopt
import cvxopt.umfpack
import cvxopt.cholmod
import cvxpy

# Funzione per matrici generiche che riceve in input la matrice del sistema lineare e restituisce:
# - Dimensione della matrice
# - Tempo impiegato per risolvere il sistema lineare (in secondi)
# - Errore relativo della soluzione
# - Memoria usata per risolvere il sistema lineare (in MB)
def matrix_solver(matrice):
    
    # Caricamento matrice A
    A = scipy.io.mmread(matrice).tocsc()
    
    # Memoria usata dopo aver letto la matrice (in MB)
    user = psutil.Process(os.getpid())
    memoria_dopo_lettura_matrice = user.memory_info().rss/1e+6
    
    # Dimensione della matrice
    dimensione = A.shape[0]
    
    # Soluzione esatta, avente tutte le componenti uguali a 1
    xe = numpy.ones(A.shape[0])
    
    # Vettore dei termini noti
    b = A.dot(xe)

    # Risoluzione sistema lineare e tempo impiegato per risolverlo (in secondi)
    tempo_iniziale = time.time()
    x = scipy.sparse.linalg.spsolve(A, b)
    tempo_impiegato = time.time() - tempo_iniziale
    
    # Memoria usata dopo aver risolto il sistema lineare (in MB)
    user = psutil.Process(os.getpid())
    memoria_dopo_risoluzione_sistema = user.memory_info().rss/1e+6

    # Errore relativo della soluzione
    errore_relativo = numpy.linalg.norm(x - xe) / numpy.linalg.norm(xe)
    
    # Differenza delle 2 memorie calcolate precedentemente (in MB)
    memoria_usata = memoria_dopo_risoluzione_sistema - memoria_dopo_lettura_matrice
 
    # Stampa delle informazioni
    print("Dimensione:", dimensione)
    print("Tempo impiegato:", tempo_impiegato)
    print("Errore relativo:", errore_relativo)
    print("Memoria usata:", memoria_usata)

# Funzione per matrici simmetriche e definite positive che riceve in input la matrice del sistema lineare e restituisce:
# - Dimensione della matrice
# - Tempo impiegato per risolvere il sistema lineare (in secondi)
# - Errore relativo della soluzione
# - Memoria usata per risolvere il sistema lineare (in MB)
def matrix_solver_cholesky(matrice):
    
    # Caricamento matrice A
    A = cvxpy.interface.matrix_utilities.sparse2cvxopt(scipy.io.loadmat(matrice)['Problem']['A'][0][0])

    # Memoria usata dopo aver letto la matrice (in MB)
    user = psutil.Process(os.getpid())
    memoria_dopo_lettura_matrice = user.memory_info().rss/1e+6

    # Dimensione della matrice
    dimensione = str(A.size[0])
    
    # Soluzione esatta, avente tutte le componenti uguali a 1
    xe = cvxopt.matrix(numpy.ones([A.size[0], 1]))
    
    # Vettore dei termini noti
    b = cvxopt.sparse(A*xe)

    # Risoluzione sistema lineare e tempo impiegato per risolverlo (in secondi)
    tempo_iniziale = time.time()
    x = cvxopt.cholmod.splinsolve(A,b)
    tempo_impiegato = time.time() - tempo_iniziale
    
    # Memoria usata dopo aver risolto il sistema lineare (in MB)
    user = psutil.Process(os.getpid())
    memoria_dopo_risoluzione_sistema = user.memory_info().rss/1e+6

    # Errore relativo della soluzione
    errore_relativo = numpy.linalg.norm(x - xe) / numpy.linalg.norm(xe)

    # Differenza delle 2 memorie calcolate precedentemente (in MB)
    memoria_usata = memoria_dopo_risoluzione_sistema - memoria_dopo_lettura_matrice
    
    # Stampa delle informazioni
    print("Dimensione:", dimensione)
    print("Tempo impiegato:", tempo_impiegato)
    print("Errore relativo:", errore_relativo)
    print("Memoria usata:", memoria_usata)

# Richiamo della funzione per ogni matrice generica
# dalla più piccola alla più grande
#matrix_solver('GT01R.mtx')
#matrix_solver('TSC_OPF_1047.mtx')
#matrix_solver('ns3Da.mtx')
#matrix_solver('ifiss_mat.mtx')

# Richiamo della funzione per ogni matrice simmetrica e definita positiva
# dalla più piccola alla più grande
#matrix_solver_cholesky('nd24k.mat')
#matrix_solver_cholesky('bundle_adj.mat')
#matrix_solver_cholesky('Hook_1498.mat')
#matrix_solver_cholesky('G3_circuit.mat')
