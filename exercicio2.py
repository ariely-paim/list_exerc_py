#Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar :
#a. A menor altura do grupo;
#b. A maior altura do grupo;

alturas = []
maior = 0
menor = 500

for i in range(15):
    altura = int(input("Escreva a sua altura em cm: "))
    alturas.append(altura)
    
    if altura > maior:
        maior = altura
        
    if altura < menor:
        menor = altura
    
print("A maior altura é", {maior})
print("A menor altura é", {menor})
