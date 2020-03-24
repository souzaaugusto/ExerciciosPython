#FORMAÇÃO DOS TIPOS DE TRIANGULOS FEITA NO CURSO DE PYTHON DO PROF GUSTAVO GUANABARA

#---------Escolha dos comprimentos das retas:
r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))

#---------Resultado:
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 != r2 and r2 == r3:
    print('Esse triângulo é ISÓCELES, pois possui 2 lados iguais')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r2 != r3 and r1 == r3:
    print('Esse triângulo é ISÓCELES,  pois possui 2 lados iguais')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 and r2 != r3:
    print('Esse triângulo é ISÓCELES,  pois possui 2 lados iguais')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 and r1 == r3 and r2 == r3:
    print('Esse triângulo é EQUILÁTERO, pois possui todos lados iguais')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 != r2 and r2 != r3 and r3 != r1:
    print('Esse triângulo é ESCALENO, pois possui todos os lados diferentes')
else:
    print('Esses comprimentos não formam um triangulo')