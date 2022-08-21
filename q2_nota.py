# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
print("*******  Verificar valor válido  ******")
nota = float(input("Digite um numero de 0 a 10: "))
while (nota > 10) or (nota < 0):
    nota = float(input("Esse valor não é válido. Digite um numero de 0 a 10: "))
else:
    print("Nota informada: " + str(nota))
