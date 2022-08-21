# Faça um Programa que peça um número correspondente a um determinado ano e em seguida
# informe se este ano é ou não bissexto.
# para ser bissexto, o ano tem que ser divisível por 4 e não ser por 100, mas poe ser divsível por 4000
print("*******  Identificar ano bissexto  ******")
ano = int(input("Digite um número correspondente a um ano e descubra se é bissexto: "))
if (ano% 4 == 0 and ano % 100 != 0) or (ano%400 == 0):
    print(" O ano", ano, "é um  bissexto")
else:
    print(ano, "não é um ano bissexto!")

