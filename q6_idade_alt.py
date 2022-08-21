# Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida
print("*******  Inverter ondem de números  ******")
idades = []
alturas = []
for x in range(5):
    idades.append(int(input("Informe sua idade em anos: ")))
    alturas.append(float(input("Informe sua altura em metros: ")))

print("\n\nIdades informadas em ordem direta: " ,  idades)
print("Alturas informadas em ordem direta: " ,  alturas)
print("\n\nIdades em ordem inversa " , idades[::-1])
print("Alturas em ordem inversa " , alturas[::-1])


