import random
import time
import numpy as np

col=100
row =100 

def createMatrix(n,m):
    return [[random.randint(1, 10) for row in range(n)] for column in range(m)]

def print_matrix(matrix, decimals=3):
    for row in matrix:
        print([round(x,decimals)+0 for x in row])

def zeros_matrix(rows, cols):
    matrix = []
    while len(matrix) < rows:
        matrix.append([])
        while len(matrix[-1]) < cols:
            matrix[-1].append(0.0)
 
    return matrix

def matrix_multiply(A, B):
    A_rows = len(A)
    A_cols = len(A[0])
    B_rows = len(B)
    B_cols = len(B[0])
    if A_cols != B_rows:
        print("number of A columns must equal number of B rows")
 
    C = zeros_matrix(A_rows, B_cols)
    start_time = time.time()
    for i in range(A_rows):
        for j in range(B_cols):
            total = 0
            for k in range(A_cols):
                total += A[i][k] * B[k][j]
            C[i][j] = total
    elapsed_time = time.time() - start_time
    print("                                 AB:            ")
    print_matrix(C,3)
    print("***************************************************")
    print("TIME:")
    print(elapsed_time)

    print("***************************************************")

    return C


a = createMatrix(col,row)
b = createMatrix(col,row)

a_1 =np.array(a)
b_1 =np.array(b)
start_time1 = time.time()
c_1= a_1.dot(b_1)
elapsed_time1 = time.time() - start_time1


print("                                 A:            ")
print_matrix(a,3)
print("***************************************************")
print("                                 B:            ")
print_matrix(b,3)
print("***************************************************")
matrix_multiply(a,b)
#print("                           AB(numpy):            ")
#print_matrix(c_1,3)
print("TIME by np:")
print(elapsed_time1)









