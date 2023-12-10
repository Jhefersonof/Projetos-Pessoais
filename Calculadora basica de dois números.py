def somar(a, b):
    return a+b

def subtrair (a, b):
    return a-b

def multiplicar (a, b):
    return a*b

def dividir (a, b):
    if b != 0:
        return a/b
    else:
        return "Erro: divisao por zero"

print ('Menu de seleções | Selecione a Operação:')
print('1. Soma')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')

opçao= input('Digite o número da operação desejada: ')

n1=float(input('Digite o primeiro Número: '))
n2=float(input('Digite o segundo Número: '))

if opçao == "1":
    resultado = somar(n1, n2)
elif opçao == "2":
    resultado = subtrair(n1, n2)
elif opçao == "3":
    resultado = multiplicar(n1, n2)
elif opçao == "4":
    resultado = dividir(n1, n2)

print('Resultado: ',resultado)