import numpy as np
import pandas as pd
import pathlib
from pathlib import Path
eps1 = 0.0001


def input_data():
    print("Enter number of equations: ")
    n = int(input())
    print("Enter koef of  equations: ")
    data = []
    for j in range(n):
        data.append([float(i) for i in input().split()])
        pass
    return n, data

def output(data, n):
    Data = data.copy()
    for i in range(n):
        print("%+.7F  %+.7F  %+.7F  %+.7F  %+.7F  " % tuple(data[i]))
    print("\n")


def Jakoby(data, n, eps):
    verif_diag_cond(data, n)
    Data, Vec = np.delete(data,n,1) , np.delete(data, np.s_[:n:],1)
    D = np.diag(np.diag(Data))
    B = np.dot(-np.linalg.inv(D), Data - D)
    C = np.dot(np.linalg.inv(D), Vec)
    q = np.linalg.norm(B, ord= np.inf )
    Delta = [0]
    Solve = []
    answer = input("Enter X(0). If you enter auto it can be C: ")
    if(answer=="auto"):
        Solve.append(np.copy(C))

    else:
        Solve.append(np.array(list(map(float, answer.split()))).reshape(4,1))

    Solve.append(np.dot(B, Solve[0])+C)
    Delta.append(np.linalg.norm(Solve[1]-Solve[0], ord = np.inf))
    while 1:
        if((Delta[len(Delta)-1] < eps) and (q <= 1/2)) or (Delta[len(Delta)-1] < eps*(1-q)/q and (q > 1/2)): break
        Solve.append(np.dot(B,Solve[len(Solve)-1])+C)
        Delta.append(np.linalg.norm(Solve[len(Solve)-1]-Solve[len(Solve)-2], ord = np.inf))
    Solution = np.c_[np.matrix(np.array(Solve)), np.array(Delta)]
    # df = pd.DataFrame(Solution, columns = ['x{}'.format(i) for i in range(n)].append('delta'))
    col = ['x_{}'.format(i) for i in range(n)]
    col.append('|x(k)-x(k-1)|')
    df = pd.DataFrame(Solution, columns=col)
    print(df)
    return Solve[len(Solve)-1]


def verification (data, solution, n):
    b = [data[i][n] for i in range(n)]
    Data = np.delete(data, n, 1)
    Res = np.dot(Data, solution.reshape(n,))
    print("\nb - Ax*: ", b-Res)


    pass

def verif_diag_cond(data,n):
    key = 1
    for i in range(n):
        s = 0
        for j in data[i]: s +=abs(j)
        if (abs(data[i][i]) < s - abs(data[i][i]) - abs(data[i][n])): key = 0
        pass
    if (key):  print("\nVerification is done")
    else: print("\nVerification is false")