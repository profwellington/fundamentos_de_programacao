#!/usr/bin/env python

''' Programa - AD1.1Q1 
    Se o número for ímpar 
        * atribui o número ao raio
        * a partir do raio realiza o cálculo e exibe:
            * área
            * perímetro
    Senão
        * exibir todos os valores divisíveis do número
'''

import math


linha = input()
while linha != "":
    numero = int(linha)
    
    if ((numero % 2) != 0):
        raio = numero
        area = math.pi * (raio ** 2)
        perimetro = 2 * math.pi * raio
        print("Área e Perímetro do Círculo de Raio %d são: %.2f e %.2f"%(raio, area, perimetro))
    else:
        print("Divisores de %d são:"%numero, end="")
        for divisor in range(1, numero + 1):
            if numero % divisor == 0:
                print("", divisor, end="")
        print()
    linha = input()
