#!/usr/bin/env python

''' Programa - AD1.1Q2  
    Pergunta a quantidade número que deseja ser informar,
    Verifica é o maior e menor número
    Soma os números em uma variável
    Exibe os seguintes valores:
        * Soma
        * Média
        * Menor 
        * Maior
'''

if __name__ == '__main__':

    qtd = int(input())
    soma = menor = maior = int(input())

    for i in range(1, qtd):
        numero = int(input())
        
        if(numero < menor):
            menor = numero
        elif(numero > maior):
            maior = numero
        soma += numero
        
    print("Soma:", soma)
    print("Média: %.2f"%(soma / qtd))
    print("Menor:", menor)
    print("Maior:", maior)
