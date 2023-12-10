import random

numero_aleatorio = random.randint(1, 10)

print("Adivinhe o número entre 1 e 10.")
tentativas = 0

while True:
    tentativa = int(input("Digite sua tentativa: "))
    tentativas += 1

    if tentativa == numero_aleatorio:
        print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
        break
    elif tentativa < numero_aleatorio:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
