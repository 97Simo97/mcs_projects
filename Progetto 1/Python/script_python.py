import numpy
import scipy.io
import scipy.sparse
import scipy.sparse.linalg
import time
import os
import psutil

# Funzione che riceve in input la matrice del sistema lineare e restituisce:
# - Dimensione della matrice
# - Tempo impiegato per risolvere il sistema lineare (in secondi)
# - Errore relativo della soluzione
# - Memoria usata per risolvere il sistema lineare (in MB)
def script_python(matrice):
    
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
    
    # Per matrici generiche
    x = scipy.sparse.linalg.spsolve(A, b)
    
    # Per matrici simmetriche e definite positive (DA SISTEMARE, NON FUNZIONA)
    #R = scipy.linalg.cholesky(A)
    #y = scipy.sparse.linalg.spsolve_triangular(R.T, b)
    #x = scipy.sparse.linalg.spsolve_triangular(R, y)
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

# Richiamo della funzione per ogni matrice
# dalla più piccola alla più grande

# Matrice generica
#script_python('GT01R.mtx')

# Matrice generica
#script_python('TSC_OPF_1047.mtx')

# Matrice generica
#script_python('ns3Da.mtx')

# Matrice simmetrica e definita positiva
#script_python('nd24k.mtx')

# Matrice generica
#script_python('ifiss_mat.mtx')

# Matrice simmetrica e definita positiva
#script_python('bundle_adj.mtx')

# Matrice simmetrica e definita positiva
#script_python('Hook_1498.mtx')

# Matrice simmetrica e definita positiva
#script_python('G3_circuit.mtx')