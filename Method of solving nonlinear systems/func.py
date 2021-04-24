import numpy as np
import pandas as pd
import pathlib
from pathlib import Path
from math import *
from sympy import *

eps1 = 0.0001
def input_data():
    n = int(input("Enter number of equations: "))
    arguments = input("Enter arguments: ").split()
    print("Enter equations")
    inputs = [input() for i in range(n)]
    return n, inputs, arguments

def Solve_matrix(matrix, parametrs, arguments , n,m):
    L, L1= [], []
    for i in range(n):
        for j in range(m):
            L1.append(matrix[i][j].evalf(subs=dict(zip(arguments, parametrs))))
        L.append(L1.copy())
        L1.clear()
    M = np.array(L, dtype='float')
    return M

def Solve_vector(matrix, parametrs, arguments ,n):
    L =[]
    for i in range(n):
        L.append(matrix[i].evalf(subs=dict(zip(arguments, parametrs))))
    M = np.array(L.copy(), dtype='float')
    return M

def Newtone(n, inputs, x0,arguments, eps):
    print("Newtone method")
    solutions, deltas = [x0], [0]
    #Find F and W
    L, L1, K = [], [], []
    for i in range(n):
        for j in range(n):
             L1.append(sympify(inputs[i]).diff(arguments[j]))
        L.append(L1.copy())
        L1.clear()
        K.append(sympify(inputs[i]))
    W =np.array(L.copy())
    F = np.array(K.copy())
    L.clear(), K.clear()
    delta = np.linalg.solve(Solve_matrix(W, x0, arguments, n, n), -Solve_vector(F, x0, arguments, n))
    solutions.append(( delta +x0).copy())
    deltas.append(np.linalg.norm(delta, ord = np.inf))
    while(deltas[-1] > eps):
        delta = np.linalg.solve(Solve_matrix(W, solutions[-1], arguments, n, n), -Solve_vector(F, solutions[-1], arguments, n))
        solutions.append((delta + solutions[-1]).copy())
        deltas.append(np.linalg.norm(delta, ord=np.inf))
    Solution = np.c_[np.matrix(solutions), np.array(deltas)]
    col = arguments.copy()
    col.append('∆')
    df = pd.DataFrame(Solution, columns=col)
    print(df)

    print("\nF(x*): ", Solve_vector(F,solutions[-1] , arguments, n))

def Simple_iter(n, inputs, x0, arguments, eps):
    print("Simple iteration method")
    solutions, deltas = [x0], [0]
    # Find F and W
    L, L1, K = [], [], []
    for i in range(n):
        for j in range(n):
            L1.append(sympify(inputs[i]).diff(arguments[j]))
        L.append(L1.copy())
        L1.clear()
        K.append(sympify(inputs[i]))
    W = np.array(L.copy())
    F = np.array(K.copy())
    L.clear(), K.clear()
    if (np.linalg.norm(Solve_matrix(W, solutions[-1], arguments, n, n), ord = np.inf) < 1): print("\nVerification is done\n")
    else: print("\nVerification is not done\n")
    solutions.append(Solve_vector(F, solutions[-1], arguments, n))
    deltas.append(np.linalg.norm(solutions[-1]-solutions[-2], ord = np.inf))
    while(deltas[-1] > eps):
        solutions.append(Solve_vector(F, solutions[-1], arguments, n))
        deltas.append(np.linalg.norm(solutions[-1] - solutions[-2], ord=np.inf))
    Solution = np.c_[np.matrix(solutions), np.array(deltas)]
    col = arguments.copy()
    col.append('∆')
    df = pd.DataFrame(Solution, columns=col)
    print(df)

    print("\nF(x*): ", Solve_vector(F, solutions[-1], arguments, n)-solutions[-1])


