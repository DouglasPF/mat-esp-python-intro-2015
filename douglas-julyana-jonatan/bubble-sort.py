# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8] #Valores da Lista
print("lista original", lista) #para imprimir a lista original sem modificações
N = 20 #Numero de Elementos
for i in range(0, N-1, 1): #Andando do primeiro elemento até o penultimo de 1 em 1
    for j in range(i+1, N, 1): #Andando do elemento seguinte a 'i' até o ultimo de 1 em 1
        if lista[i] < lista[j]:
            continue
        else:
            temp = lista[i] #Para inverter os valores
            lista[i] = lista[j]
            lista[j] = temp
print("lista em ordem crescente", lista) #para imprimir a lista em ordem crescente com modificações

#Para selecionar o primeiro elemento da lista 'lista[0]'
#Para selecionar os cincos primeiros elementos da lista 'lista[0:4]'




 
           
            

    