#Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500.

soma = sum(i for i in range(1, 500) if i%3 ==0)
print(soma)
