from numpy import *
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

def Gauss(data, n, eps):
    # Forward
    det = 1
    solution1 = []
    key1 = 1
    problem_equations = []
    output(data, n)
    for k in range(n - 1):
        for i in range(k + 1, n):
            multiplier = data[i][k] / data[k][k]
            data[i][k] = 0
            for j in range(k + 1, n + 1):
                data[i][j] -= data[k][j] * multiplier
            if (abs(data[i][k + 1]) < eps):
                problem_equations.append(i)
                pass
            pass
        # solve problem of 0
        if (len(problem_equations) == n - k - 1):
            print("Infinity solution")
            key1 = 0
            break
        for i in problem_equations:
            data.append(data[i])
            data.pop(i)
            pass
        output(data, n)
        pass
    for i in range(n):
        det *= data[i][i]
    # Back
    if (key1):
        solution1.append(data[n - 1][n] / data[n - 1][n - 1])
        for k in range(1, n + 1):
            sum = data[n - k - 1][n]
            for i in range(k):
                sum -= data[n - k - 1][n - 1 - i] * solution1[i]
            solution1.append(sum / data[n - 1 - k][n - 1 - k])

        solution1.pop(n)
        solution1.reverse()
        solution1.append(det)
        print("          ", end="")
        for i in range(n):
            print("x", i + 1, end="      ")
            pass
        print("det")
        print("Solution: ", end="")
        for i in solution1:
            print("%.5f" % i, end=" ")
            pass
        print("")

        pass
    return solution1


def Gauss_main_element(data, n, eps):
    det = 1
    permutation = 0
    solution2 = []
    key2 = 1
    problem_equations2 = []
    output(data, n)
    # Forward
    for k in range(n - 1):
        max = k
        for i in range(k + 1, n):
            if (abs(data[max][k]) < abs(data[i][k])): max = i
        if (max != k):
            data.append(data[k])
            data[k] = data[max]
            data[max] = data[-1]
            data.pop()
            permutation += 1
            pass
        output(data, n)

        for i in range(k + 1, n):
            multiplier = data[i][k] / data[k][k]
            data[i][k] = 0
            for j in range(k + 1, n + 1):
                data[i][j] -= data[k][j] * multiplier
            if (abs(data[i][k + 1]) < eps):
                problem_equations2.append(i)
                pass
            pass
        # solve problem of 0
        if (len(problem_equations2) == n - k - 1):
            print("Infinity solution")
            key2 = 0
            break
        for i in problem_equations2:
            data.append(data[i])
            data.pop(i)
            pass
        output(data, n)

        pass
    for i in range(n):
        det *= data[i][i]
    if(permutation%2 != 0): det *= -1
    # Back
    if (key2):
        solution2.append(data[n - 1][n] / data[n - 1][n - 1])
        for k in range(1, n + 1):
            sum = data[n - k - 1][n]
            for i in range(k):
                sum -= data[n - k - 1][n - 1 - i] * solution2[i]
            solution2.append(sum / data[n - 1 - k][n - 1 - k])

        solution2.pop(n)
        solution2.reverse()
        solution2.append(det)
        print("          ", end="")
        for i in range(n):
            print("x",i+1,end="      ")
            pass
        print("det")
        print("Solution: ", end="")
        for i in solution2:
            print("%.5f" % i, end=" ")
        print("")
        pass
    return solution2


def progonka (data, n, eps):
    det = 1
    #verification of sufficient conditions
    key = 1
    if(abs(data[0][0]) <= abs(data[0][1]) or abs(data[n-1][n-1]) <= abs(data[n-1][n-2])): key = 0
    for i in range(1,n-1):
        if((abs(data[i][i]) <= abs(data[i][i-1]) + abs(data[i][i+1])) or (data[i][i-1] == 0) or (data[i][i+1] == 0)): key = 0

    if (key):
        #forward propagation
        alfa = []
        beta = []
        alfa.append(data[0][n]/data[0][0])
        beta.append(-data[0][1]/data[0][0])
        for i in range(1,n-1):
            beta.append(-data[i][i+1]/(data[i][i]+data[i][i-1]*beta[i-1]))
            alfa.append((data[i][n]-data[i][i-1]*alfa[i-1])/(data[i][i]+data[i][i-1]*beta[i-1]))
        beta.append(0)
        alfa.append((data[n-1][n]-data[n-1][n-2]*alfa[n-2])/(data[n - 1][n - 1]+data[n-1][n-2]*beta[n-2]))

        #back propagation
        solution = []
        solution.append(alfa[n-1])
        for i in range(1,n+1):
            solution.append(beta[n-i]*solution[i-1]+alfa[n-i])
            pass
        solution.reverse()
        solution.pop()
        print("Solution: ", end="")
        for i in solution:
            print("%.5f" % i, end=" ")
    else:
        print("\n verification of sufficient conditions is false")
    return solution

def output(data, n):
    Data = data.copy()
    for i in range(n):
        print("%+.7F  %+.7F  %+.7F  %+.7F  %+.7F  " % tuple(data[i]))
    print("\n")



def verification (data, solution, n):
    b = []
    for i in data:
        b.append(i[n])
        i.pop()
        pass
    d = array(data, float)
    s = array(solution, float)
    s.reshape(n,1)
    b = array(b)
    b.reshape(n,1)
    if (all((dot(d,s) - b < eps1))):
        print("\nVerification is done")
    else:
        print("Verification is not successfull")

    pass