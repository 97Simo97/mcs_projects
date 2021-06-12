import math
import time
import numpy
import scipy.fftpack

# Funzione che effettua la DCT1 su un vettore
def my_dct1(vector):

    dct1 = []

    for k in range(0, len(vector)):
        sum = 0

        if k == 0:
            coeff = math.sqrt(1 / len(vector))
        else:
            coeff = math.sqrt(2 / len(vector))

        for j in range(0, len(vector)):
            var_dct = (vector[j] * math.cos(math.pi * k * (2 * j + 1) / (2 * len(vector))))
            sum += var_dct

        dct1.append(coeff * sum)

    return dct1

# Funzione che effettua la DCT2 su una matrice utilizzando la DCT1 per righe e per colonne
def my_dct2(matrix):

    #DCT1 per righe
    dctrighe = my_dct1(numpy.transpose(matrix))

    #DCT1 per colonne
    dct2 = my_dct1(numpy.transpose(dctrighe))

    return dct2

# Test di scaling monodimensionale
def test_one_dim():

    vector = [231, 32, 233, 161, 24, 71, 140, 245]

    print("Test DCT1:")

    test_scipy_dct = scipy.fftpack.dct(vector, type = 2, norm='ortho')
    print("DCT1 di Scipy:")
    for i in test_scipy_dct:
        print("{:.2e}".format(i))

    print("----------------------------------------")

    test_my_dct = my_dct1(vector)
    print("DCT1 implementata da noi:")
    for i in test_my_dct:
        print("{:.2e}".format(i))

# Test di scaling bidimensionale
def test_two_dim():

    matrix = [[231, 32, 233, 161, 24, 71, 140, 245],
                   [247, 40, 248, 245, 124, 204, 36, 107],
                   [234, 202, 245, 167, 9, 217, 239, 173],
                   [193, 190, 100, 167, 43, 180, 8, 70],
                   [11, 24, 210, 177, 81, 243, 8, 112],
                   [97, 195, 203, 47, 125, 114, 165, 181],
                   [193, 70, 174, 167, 41, 30, 127, 245],
                   [87, 149, 57, 192, 65, 129, 178, 228]]

    print("Test DCT2:")

    test_scipy_dct = scipy.fftpack.dctn(matrix, type = 2, norm = 'ortho')
    print("DCT2 di Scipy:")
    for i in range(0,8):
        for j in range(0,8):
            print("{:.2e}".format(test_scipy_dct[i][j]))

    print("----------------------------------------")

    test_my_dct = my_dct2(matrix)
    print("DCT2 implementata da noi:")
    for i in range(0,8):
        for j in range(0,8):
            print("{:.2e}".format(test_my_dct[i][j]))

# Main
def main():

    # Esecuzione test
    test_one_dim()
    print("----------------------------------------")
    test_two_dim()
    print("----------------------------------------")

    values_of_dimension = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
    scipy_dct2_time = []
    my_dct2_time = []    

    # Esecuzione delle DCT2 e salvataggio dei tempi di esecuzione
    for x in values_of_dimension:
        matrix = numpy.random.randint(256, size=(x,x))   

        time1 = time.time()
        time1 = float(time1)
        scipy.fftpack.dctn(matrix, type = 2, norm = 'ortho')
        time2 = time.time()
        time2 = float(time2)
        time3 = time2 - time1
        scipy_dct2_time.append(time3)

        time4 = time.time()
        time4 = float(time4)
        my_dct2(matrix)
        time5 = time.time()
        time5 = float(time5)
        time6 = time5 - time4
        my_dct2_time.append(time6)

    # Stampa dei tempi delle DCT2
    print("Tempi DCT2 di Scipy:")
    print(scipy_dct2_time)
    print("----------------------------------------")
    print("Tempi DCT2 implementata da noi:")
    print(my_dct2_time)

if __name__ == "__main__":
    main()