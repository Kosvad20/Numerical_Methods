from func import *

eps = 0.00001

#main
l = [float(i) for i in input("Enter x(0): ").split()]
x0 = np.asarray(l)
n, inputs, arguments = input_data()
Newtone(n, inputs, x0, arguments, eps)
# Simple_iter(n, inputs, x0, arguments, eps)