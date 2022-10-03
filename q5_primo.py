#Faça um programa que gera uma lista dos números primos existentes
# entre 1 e um número inteiro informado pelo usuário.
print("*******  Verificar primos existentes  ******")
numero = int(input("digite um numero para saber todos os primos existentes menores que esse número "))
  
    
n = int(input("Digite um número para saber os seus divisores primos: "))
lista= []
for i in range(1, n + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            lista.append(i)
print(lista)
