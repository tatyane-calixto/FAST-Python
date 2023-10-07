a = float(input('Digite o valor de A :'))
b = float(input('Digite o valor de B :'))
c = float(input('Digite o valor de C :'))
area_tr = (a * c)/2
raio_circ = 3.14 * c ** 2
area_trap = (a + b) * c
area_quad = b ** 2
area_ret = a * b

print('A área do triângolo é: {0:.2f}').format(area_tr)
print('A área do raio é: {0:.2f}').format(raio_circ)
print('A área do trapézio é: {0:.2f}').format(area_trap)
print('A área do quadrado é: {0:.2f}').format(area_quad)
print('A área do retângulo é : {0:.2f}').format(area_ret)