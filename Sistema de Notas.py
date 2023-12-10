nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))
nota_3 = float(input("Insira a terceira nota: "))
nota_4 = float(input("Insira a quarta nota: "))

if nota_1 > nota_2 and nota_3 and nota_4:
    print(f"A maior nota é {nota_1}")
elif nota_2 > nota_3 and nota_4:
    print(f"A maior nota é {nota_2}")
elif nota_3 > nota_4:
    print(f"A maior nota é {nota_3}")
else:
    print(f"A maior nota é {nota_4}")


if nota_1 < nota_2 and nota_3 and nota_4:
    print(f"A menor nota é {nota_1}")
elif nota_2 < nota_3 and nota_4:
    print(f"A menor nota é {nota_2}")
elif nota_3 < nota_4:
    print(f"A menor nota é {nota_3}")
else:
    print(f"A menor nota é {nota_4}")

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print (f"A média do aluno é {media}")