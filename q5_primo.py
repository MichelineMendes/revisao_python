#Faça um programa que gera uma lista dos números primos existentes
# entre 1 e um número inteiro informado pelo usuário.
print("*******  Verificar primos existentes  ******")
numero = int(input("digite um numero para saber todos os primos existentes menores que esse número "))
for x in range(2, numero+1):
    if x ==2 or x%2 !=0:
       print(x, end= " , ")
