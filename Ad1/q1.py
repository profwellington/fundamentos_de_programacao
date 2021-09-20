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


def circulo(raio):
    area = math.pi * (raio ** 2)
    perimetro = 2 * math.pi * raio
    return([raio, area, perimetro])


def divisor(numero):
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            print("", divisor, end="")
        print()


def main(numero):
    if ((numero % 2) != 0):
        circulo_resultado = circulo(numero)            
        print("Área e Perímetro do Círculo de Raio %d são: %.2f e %.2f"%
              (circulo_resultado[0], circulo_resultado[1], circulo_resultado[2]))
        return circulo_resultado
    else:
        print("Divisores de %d são:"%numero, end="")
        divisor(numero)
        return numero
        
if __name__ == '__main__':
    main(3)
    