from func import *

eps = 0.0001

#main
n, data = input_data()
#Gauss_main_element(data, n, eps)
#
# print("Gauss")
# s1 = Gauss_main_element(data.copy(),n, eps )
# s1.pop()
# verification(data.copy(), s1,n)

print("Progonka")
s2 = progonka(data.copy(),n, eps)
verification(data.copy(), s2,n)
