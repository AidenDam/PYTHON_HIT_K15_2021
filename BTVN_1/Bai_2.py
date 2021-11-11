from math import sqrt, sin, exp

x = int(input('Nhập x: '))

print('Giá trị biểu thức: ', (x**2 + exp(x) + sin(x)) / sqrt(x**2+1))