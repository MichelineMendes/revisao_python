#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
print("*******  Transformar temperatura de °F para C  ******")
f = float(input("Informe a temperatura em graus Fahrenheit:  "))
tc = round(5 * ((f-32) / 9), 1)
print("A temperatura em graus Celsius é : " + str(tc))