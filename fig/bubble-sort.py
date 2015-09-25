# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8] #Valores da Lista
plt.figure() 
#Criamos uma figura vazia
plt.plot(range(0,20), lista, 'ok')
#Definimos x como 'range(0,20)' e y como a lista original, antes de ser modificada pelo algoritmo
plt.title("Lista Original")
#Título do Gráfico
plt.xlabel("Posição na lista")
#Nomeamos X
plt.ylabel("Valores da lista")
#Nomeamos Y
plt.savefig("bubble-inicio.png")
#Salvamos a figura
plt.close()
#Fechamos a figura
print("lista original", lista) #para imprimir a lista original sem modificações
a = 0
N = 20 #Numero de Elementos
for i in range(0, N-1, 1): #Andando do primeiro elemento até o penultimo de 1 em 1
    for j in range(i+1, N, 1): #Andando do elemento seguinte a 'i' até o ultimo de 1 em 1
        if lista[i] < lista[j]:
            continue
        else:
            temp = lista[i] #Para inverter os valores
            lista[i] = lista[j]
            lista[j] = temp
            plt.figure()
            plt.plot(range(0,20), lista, 'ok')
            plt.title("Lista Em Cada Troca")
            plt.xlabel("Posição na lista")
            plt.ylabel("Valores da lista")        
            a = a + 1
            plt.savefig("bubble-troca{}.png".format(a))
print("lista em ordem crescente", lista) #para imprimir a lista em ordem crescente com modificações
plt.figure() 
plt.plot(range(0,20), lista, 'ok')
plt.title("Lista Em Ordem Crescente")
plt.xlabel("Posição na lista")
plt.ylabel("Valores da lista")
plt.savefig("bubble-fim.png")
plt.close()


print("cinco menores valores", lista[0:5]) #usamos esse comando para imprimir apenas os cinco menores valores da lista em ordem crescente, e o nomeamos como 'cinco menores valores'
print("cinco maiores valores", lista[15:20]) #usamos esse comando para imprimir apenas os cinco maiores valores da lista em ordem crescente, e o nomeamos como 'cinco maiores valores'

#Para selecionar o primeiro elemento da lista 'lista[0]'
#Para selecionar os cincos primeiros elementos da lista 'lista[0:4]'







           
            

    