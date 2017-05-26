import numpy as np
import scipy.linalg as sla
import time
import matplotlib.pyplot as plt
%matplotlib inline
from mpl_toolkits.mplot3d import Axes3D

#first  how
PD = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
A = np.array([[2, 7, 3], [7, 9, 4], [3, 4, 7]])
b = np.array([[1], [2], [3]])
c = np.array([1, 2, 3])

#1.1
def maSolveNaive(A, b):
    invA = sla.inv(A)
    return invA.dot(b)


# 2.1
y = sla.solve(PD, c)
print(y)

# 2.2
def holsolve(A, b):
    H = A.T.dot(A) #???
    K = sla.cholesky(H)
    x = sla.solve_triangular(K, b)
    return x

def solveLU(A, b):
    P, L, U = sla.lu(PD)
    y = sla.solve_triangular(L, b, lower=True)
    x = sla.solve_triangular(U, y)
    return x

#print (sla.lu(PD))
print (maSolveNaive(PD, b))
print (holsolve(A, b))
print(solveLU(A, b))

def slow_function(n):
    for i in range(n):
        M = sla.hilbert(200)
        Q, R = sla.qr(M)


#the_time = %timeit slow_function(2)
#the_time