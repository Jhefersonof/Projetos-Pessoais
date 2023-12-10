import string

letras_maiusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = string.punctuation

print("Bem Vindo ao gerador de Senha!")

quantidade_letras_maiusculas = int(input("Quantas letras maiúsculas você deseja na senha? "))
quantidade_letras_minusculas = int(input("Quantas letras minúsculas você deseja na senha? "))
quantidade_numeros = int(input("Quantos números você deseja na senha? "))
quantidade_simbolos = int(input("Quantos símbolos você deseja na senha? "))
comprimento_senha = int(input("Qual é o comprimento total da senha? "))

caracteres_escolhidos = []

if quantidade_letras_maiusculas > 0:
    caracteres_escolhidos.extend(letras_maiusculas)

if quantidade_letras_minusculas > 0:
    caracteres_escolhidos.extend(letras_minusculas)

if quantidade_numeros > 0:
    caracteres_escolhidos.extend(numeros)

if quantidade_simbolos > 0:
    caracteres_escolhidos.extend(simbolos)

if comprimento_senha < (quantidade_letras_maiusculas + quantidade_letras_minusculas + quantidade_numeros + quantidade_simbolos):
    print("O comprimento da senha é muito curto para as preferências fornecidas.")
    exit()

import random

senha = []

senha.append(random.choice(letras_maiusculas))
senha.append(random.choice(letras_minusculas))
senha.append(random.choice(numeros))
senha.append(random.choice(simbolos))

caracteres_faltantes = comprimento_senha - 4
senha.extend(random.choice(caracteres_escolhidos) for _ in range(caracteres_faltantes))
random.shuffle(senha)
senha_gerada = ''.join(senha)

print("Sua senha gerada é:", senha_gerada)
