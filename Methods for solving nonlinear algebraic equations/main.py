import math
import matplotlib.pyplot as plt
import numpy as np
eps0 = 0.001        # step when finding intervals
eps = 0.00001

def f(x, list):
    n = len(list)
    s = 0
    for i in range(n):
        s = s + list[i] * x**(i)
        pass
    return s

def division_in_half(intervals, eps, delta, koef):
    solution = []
    indicator = 0
    for interval in intervals:
        a = interval[0]
        b = interval[1]
        while 1:
            c = (a+b)/2.0
            if b-a < 2*eps :
                solution.append(c)
                indicator +=1
                break
            f_c = f(c, koef)
            if (abs(f_c) < delta):
                solution.append(c)
                indicator += 1
                break
            if(indicator == 0 ):
                print(f"interval [{a, b}] , f(left) = {f(a, koef)}, f(right) = {f(b, koef)} ")
            if(f(a, koef)*f_c < 0):
                b = c
            else:
                a = c
    return solution

def derivative_of_polinom(x, list, k):
    lis = list.copy()

    for el in range(k):
        new_koef = []
        n = len(lis)
        for i in range(n-1):
            new_koef.append(lis[i+1]*(i+1))
            pass
        lis.clear()
        lis.extend(new_koef)
    s = 0
    for i in range(len(lis)):
        s = s + lis[i]*x**(i)
    return s

def hord_method (intervals, eps, delta, koef_old):
    koef = koef_old.copy()
    solution = []
    indicator = 0
    for interval in intervals:
        a = interval[0]
        b = interval[1]
        if(derivative_of_polinom((b+a)/2, koef, 2) < 0 ):
            for i in koef:
                i = -i

        if (f(a, koef) > 0):
            while 1:
                b_new = b - f(b, koef)*(b-a)/(f(b, koef)-f(a, koef))
                if(abs(b_new - b)<eps or abs(f(b_new, koef))<delta):
                    solution.append(b_new)
                    indicator +=1
                    break
                b = b_new
                if (indicator == 0):
                    print(f"interval [{a, b}] , f(left) = {f(a, koef)}, f(right) = {f(b, koef)} ")

        else:
            while 1:
                a_new = a - f(a, koef) * (b - a) / (f(b, koef) - f(a, koef))
                if (abs(a_new - a) < eps or abs(f(a_new, koef)) < delta):
                    solution.append(a_new)
                    indicator += 1
                    break
                a = a_new
                if (indicator == 0):
                    print(f"interval [{a, b}] , f(left) = {f(a, koef)}, f(right) = {f(b, koef)} ")

    return solution

def newton_method(intervals, eps, delta, koef):
    solution = []
    indicator = 0
    for interval in intervals:
        a = interval[0]
        b = interval[1]
        c = a
        while 1:
            if (f(c, koef) * derivative_of_polinom(c, koef, 2) > 0):
                break
            c = c + eps0
            pass
        while 1:

            c_new = c - f(c, koef)/derivative_of_polinom(c, koef, 1)
            if (abs(c_new - c) < eps or abs(f(c_new, koef)) < delta):
                solution.append(c_new)
                indicator +=1
                break
            c = c_new
            if (indicator == 0):
                print(f"interval [{c, b}] , f(left) = {f(c, koef)}, f(right) = {f(b, koef)} ")


    return solution



# input od data
a = [float(i) for i in input("Enter the list of koef : ").split()]
n = len(a) -1
if (a[0] < 0):
    for i in a:
        i = -i
        pass
    pass
a.reverse()

# Theorem 3
inf_interval_pos = 1/(1+float(max(a[1:n+1]))/abs(a[0]))
sup_interval_pos = 1 + float(max(a[:n]))/abs(a[n])
inf_interval_neg = -sup_interval_pos
sup_interval_neg = -inf_interval_pos

# Find intervals for each solve
intervals = []
i = inf_interval_neg
f_last = 0

while i < sup_interval_neg:
    f_cur = f(i, a)
    if (f_last * f_cur < 0):
        intervals.append([i - eps0, i])
        pass
    f_last = f_cur
    i = i+eps0
    pass

i = inf_interval_pos
f_last = 0
while i < sup_interval_pos:
    f_cur = f(i, a)
    if (f_last * f_cur < 0):
        intervals.append([i- eps0,i])
        pass
    f_last = f_cur
    i = i+eps0
    pass

# print solution
print(intervals)
print("solution 1:", division_in_half(intervals, eps, eps, a))
print("solution 2:", hord_method(intervals, eps, eps, a))
print("solution 3:", newton_method(intervals, eps, eps, a))

# Draw plot

x = np.linspace(-3, 5, 10000)
y = f(x,a)
fig, ax = plt.subplots()
ax.plot(x, y, color="blue", label="f(x)")
plt.plot([-3,5],[0,0], color='g')
ax.legend()
plt.axis([-3, 5, -10, 30])
plt.show()