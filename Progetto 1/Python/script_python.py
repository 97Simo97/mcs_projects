import os
import time
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
def risolutore_matrici_generiche(matrice):
    
    # Caricamento matrice A
    A = scipy.io.mmread(matrice).tocsc()
    
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

    # Errore relativo della soluzione
    errore_relativo = numpy.linalg.norm(x - xe) / numpy.linalg.norm(xe)
 
    # Stampa delle informazioni
    print("Dimensione:", dimensione)
    print("Tempo impiegato:", tempo_impiegato)
    print("Errore relativo:", errore_relativo)

# Funzione per matrici simmetriche e definite positive che riceve in input la matrice del sistema lineare e restituisce:
# - Dimensione della matrice
# - Tempo impiegato per risolvere il sistema lineare (in secondi)
# - Errore relativo della soluzione
def risolutore_matrici_simmmetriche_definite_positive(matrice):
    
    # Caricamento matrice A
    A = cvxpy.interface.matrix_utilities.sparse2cvxopt(scipy.io.loadmat(matrice)['Problem']['A'][0][0])

    # Dimensione della matrice
    dimensione = str(A.size[0])
    
    # Soluzione esatta, avente tutte le componenti uguali a 1
    xe = cvxopt.matrix(numpy.ones([A.size[0], 1]))
    
    # Vettore dei termini noti
    b = cvxopt.sparse(A*xe)

    # Risoluzione sistema lineare e tempo impiegato per risolverlo (in secondi)
    tempo_iniziale = time.time()
    x = cvxopt.cholmod.splinsolve(A, b)
    tempo_impiegato = time.time() - tempo_iniziale

    # Errore relativo della soluzione
    errore_relativo = numpy.linalg.norm(x - xe) / numpy.linalg.norm(xe)
    
    # Stampa delle informazioni
    print("Dimensione:", dimensione)
    print("Tempo impiegato:", tempo_impiegato)
    print("Errore relativo:", errore_relativo)

# Richiamo della funzione per ogni matrice generica
# dalla più piccola alla più grande
#risolutore_matrici_generiche('GT01R.mtx')
#risolutore_matrici_generiche('TSC_OPF_1047.mtx')
#risolutore_matrici_generiche('ns3Da.mtx')
#risolutore_matrici_generiche('ifiss_mat.mtx')

# Richiamo della funzione per ogni matrice simmetrica e definita positiva
# dalla più piccola alla più grande
#risolutore_matrici_simmmetriche_definite_positive('nd24k.mat')
#risolutore_matrici_simmmetriche_definite_positive('bundle_adj.mat')
#risolutore_matrici_simmmetriche_definite_positive('Hook_1498.mat')
#risolutore_matrici_simmmetriche_definite_positive('G3_circuit.mat')
