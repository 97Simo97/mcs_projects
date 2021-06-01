% Funzione che riceve in input la matrice del sistema lineare e restituisce:
% - Dimensione della matrice
% - Tempo impiegato per risolvere il sistema lineare (in secondi)
% - Errore relativo della soluzione
% - Memoria usata per risolvere il sistema lineare (in MB)
function [dimensione,tempo_impiegato,errore_relativo,memoria_usata] = script_matlab(matrice)

% Per comodità nel visualizzare i dati
format shortG;

% Caricamento matrice A
matrix = load(matrice);
A = matrix.Problem.A;

% Memoria usata dopo aver letto la matrice (in MB)
user = memory;
memoria_dopo_lettura_matrice = user.MemUsedMATLAB/1e6;

% Dimensione della matrice
dimensione = size(A,1);

% Soluzione esatta, avente tutte le componenti uguali a 1
xe = ones(dimensione,1);

% Vettore dei termini noti
b = A*xe;

% Risoluzione sistema lineare e tempo impiegato per risolverlo (in secondi)
tic;
x = A\b;
tempo_impiegato=toc;

% Memoria usata dopo aver risolto il sistema lineare (in MB)
user = memory;
memoria_dopo_risoluzione_sistema = user.MemUsedMATLAB/1e6;

% Errore relativo della soluzione
errore_relativo = norm(x - xe)/norm(xe);

% Differenza delle 2 memorie calcolate precedentemente (in MB)
memoria_usata = memoria_dopo_risoluzione_sistema - memoria_dopo_lettura_matrice;

% Richiamo della funzione per ogni matrice generica
% dalla più piccola alla più grande                                                                                                                                                                                    
%[Dimensione,Tempo,Errore,Memoria] = script_matlab("GT01R")                                                                                                                                                                                
%[Dimensione,Tempo,Errore,Memoria] = script_matlab("TSC_OPF_1047")
%[Dimensione,Tempo,Errore,Memoria] = script_matlab("ns3Da")                                                                                                                                                                                   %[Dimensione,Tempo,Errore,Memoria] = script_matlab("ns3Da")
%[Dimensione,Tempo,Errore,Memoria] = script_matlab("ifiss_mat")

% Richiamo della funzione per ogni matrice simmetrica e definita positiva
% dalla più piccola alla più grande
%[Dimensione,Tempo,Errore,Memoria] = script_matlab("nd24k")                                                                                                                                                                                                                                                                                                                                                                       
%[Dimensione,Tempo,Errore,Memoria] = script_matlab("bundle_adj")                                                                                                                                                                                  
%[Dimensione,Tempo,Errore,Memoria] = script_matlab("Hook_1498")                                                                                                                                                                                 
%[Dimensione,Tempo,Errore,Memoria] = script_matlab("G3_circuit")