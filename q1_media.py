#1 - Faça um programa para leitura de três notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
#a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#b) A mensagem  "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#c) A mensagem  "Aprovado com Distinção", se a média for igual a 10.


print("*******  Cálculo da média do aluno  ******")
n1 = float(input("Digite a primeira nota do aluno:  "))
n2 = float(input("digite a segunda nota do aluno:  "))
n3 = float(input("Digite a terceira nota do aluno:  "))

media = round((n1 + n2 + n3) / 3, 1)

if media >= 7.0 and media < 10:
    print("Aprovado com média: " + str(media))
elif media >= 10:
    print("Aprovado com Distinção! Média: " + str(media))
else:
    print("Reprovado. Média:" + str(media))


