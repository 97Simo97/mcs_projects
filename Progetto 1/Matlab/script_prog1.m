function [len, tempo_impiegato,err_relativo,memoria_usata] = script_prog1(matrice)
Matrix = load(matrice);

A = Matrix.Problem.A;

len = size(A,1);

xe = ones(len,1);

b = A * xe;

tic

x = A\b;

toc

tempo_impiegato = toc;

err_relativo = norm(x - xe)/norm(xe);

usr = memory;
format shortG
memoria_usata = usr.MemUsedMATLAB/1e6;
