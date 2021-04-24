from func import *

eps = 0.00001

#main
n, data = input_data()
solution = Jakoby(data, n, eps)
verification (data, solution, n)