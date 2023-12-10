#Unidade de Temperatura
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

#Unidades de Massa
def quilometros_para_metros(quilometros):
    return quilometros * 1000

def metros_para_quilometros(metros):
    return metros / 1000

def metros_para_centimetros(metros):
    return metros * 100

def centimetros_para_metros(centimetros):
    return centimetros / 100

def metros_para_decimetros(metros):
    return metros * 10

def decimetros_para_metros(decimetros):
    return decimetros / 10

def metros_para_milimetros(metros):
    return metros * 1000

def milimetros_para_metros(milimetros):
    return milimetros / 1000

#Unidades de volume
def metro_cubico_para_litro(metro_cubico):
    return metro_cubico * 1000

def litro_para_metro_cubico(litro):
    return litro / 1000

def metro_cubico_para_mililitro(metro_cubico):
    return metro_cubico * 1000000

def mililitro_para_metro_cubico(mililitro):
    return mililitro / 1000000

#Unidades de pressão
def atmosfera_para_pascal(atm):
    return atm * 101325

def pascal_para_atmosfera(pa):
    return pa / 101325

def atmosfera_para_mmHg(atm):
    return atm * 760

def mmHg_para_atmosfera(mmHg):
    return mmHg / 760

def atmosfera_para_cmHg(atm):
    return atm * 76

def cmHg_para_atmosfera(cmHg):
    return cmHg / 76

def pascal_para_quilopascal(pa):
    return pa / 1000

def quilopascal_para_pascal(kpa):
    return kpa * 1000

#Unidades de comprimento
def quilometros_para_metros(quilometros):
    return quilometros * 1000

def metros_para_quilometros(metros):
    return metros / 1000

def metros_para_centimetros(metros):
    return metros * 100

def centimetros_para_metros(centimetros):
    return centimetros / 100

def metros_para_decimetros(metros):
    return metros * 10

def decimetros_para_metros(decimetros):
    return decimetros / 10

def metros_para_milimetros(metros):
    return metros * 1000

def milimetros_para_metros(milimetros):
    return milimetros / 1000

#Unidades de energia na forma de calor
def joule_para_caloria(joule):
    return joule / 4.184

def caloria_para_joule(caloria):
    return caloria * 4.184

def quilojoule_para_joule(kj):
    return kj * 1000

def joule_para_quilojoule(joule):
    return joule / 1000

def quilocaloria_para_caloria(kcal):
    return kcal * 1000

def caloria_para_quilocaloria(caloria):
    return caloria / 1000

#Unidades de tempo
def hora_para_minuto(hora):
    return hora * 60

def minuto_para_hora(minuto):
    return minuto / 60

def hora_para_segundo(hora):
    return hora * 3600

def segundo_para_hora(segundo):
    return segundo / 3600

def minuto_para_segundo(minuto):
    return minuto * 60

def segundo_para_minuto(segundo):
    return segundo / 60 
#Mol (quantidade de matéria)
def mol_para_mol(mol):
    return mol

def mol_para_quilomol(mol):
    return mol * 0.001

def quilomol_para_mol(quilomol):
    return quilomol * 1000

# Função principal
def main():
    print("Bem-vindo ao Conversor de Unidades!")

    while True:
        print("\nEscolha uma categoria de conversão:")
        print("1. Temperatura (Celsius, Fahrenheit, Kelvin)")
        print("2. Massa (Tonelada, Quilograma, Grama, Miligrama)")
        print("3. Volume (Metro Cúbico, Litro, Mililitro)")
        print("4. Pressão (Atmosfera, Milímetro de Mercúrio, Centimetro de Mercúrio, Pascal, Quilopascal)")
        print("5. Comprimento (Quilômetro, Metro, Centímetro, Decímetro, Milímetro)")
        print("6. Energia (Joule, Quilojoule, Calorias, Quilocalorias)")
        print("7. Tempo (Hora, Minuto, Segundo)")
        print("8. Quantidade de Matéria (Mol, quilomol)")
        print("9. Sair")

        escolha = input("Digite o número da categoria: ")

        if escolha == '1':  # Unidade de Temperatura
            valor = float(input("Digite o valor: "))
            origem = input("Digite a unidade de origem (C, F, K): ").upper()
            destino = input("Digite a unidade de destino (C, F, K): ").upper()

            if origem == 'C' and destino == 'F':
                resultado = celsius_para_fahrenheit(valor)

            elif origem == 'F' and destino == 'C':
                resultado = fahrenheit_para_celsius(valor)

            elif origem == 'C' and destino == 'K':
                resultado = celsius_para_kelvin(valor)

            elif origem == 'K' and destino == 'C':
                resultado = kelvin_para_celsius(valor)

            elif origem == 'F' and destino == 'K':
                resultado = fahrenheit_para_kelvin(valor)

            elif origem == 'K' and destino == 'F':
                resultado = kelvin_para_fahrenheit(valor)
            """else:
                print("Opção de conversão inválida.")"""

            print(f"{valor} {origem} = {resultado} {destino}")

        elif escolha == '2':  # Unidades de Massa
            valor = float(input("Digite o valor: "))
            origem = input("Digite a unidade de origem (t, kg, g, mg): ").lower()
            destino = input("Digite a unidade de destino (t, kg, g, mg): ").lower()

            if origem == 't' and destino == 'kg':
                resultado = toneladas_para_quilogramas(valor)

            elif origem == 'kg' and destino == 't':
                resultado = quilogramas_para_toneladas(valor)

            elif origem == 'kg' and destino == 'g':
                resultado = quilogramas_para_gramas(valor)

            elif origem == 'g' and destino == 'kg':
                resultado = gramas_para_quilogramas(valor)

            elif origem == 'kg' and destino == 'mg':
                resultado = quilogramas_para_miligramas(valor)

            elif origem == 'mg' and destino == 'kg':
                resultado = miligramas_para_quilogramas(valor)

            """else:
                print("Opção de conversão inválida.")"""

            print(f"{valor} {origem} = {resultado} {destino}")

        elif escolha == '3':  # Unidades de Volume
            valor = float(input("Digite o valor: "))
            origem = input("Digite a unidade de origem (m³, L, dm³, mL, cm³): ").lower()
            destino = input("Digite a unidade de destino (m³, L, dm³, mL, cm³): ").lower()

            if origem == 'm³' and destino == 'L':
                resultado = metro_cubico_para_litro(valor)

            elif origem == 'L' and destino == 'm³':
                resultado = litro_para_metro_cubico(valor)

            elif origem == 'm³' and destino == 'mL':
                resultado = metro_cubico_para_mililitro(valor)

            elif origem == 'mL' and destino == 'm³':
                resultado = mililitro_para_metro_cubico(valor)

            """else:
                print("Opção de conversão inválida.")"""

            print(f"{valor} {origem} = {resultado} {destino}")


        elif escolha == '4':  # Unidades de Pressão

            valor = float(input("Digite o valor: "))
            origem = input("Digite a unidade de origem (atm, mmHg, cmHg, Pa, kPa): ").lower()
            destino = input("Digite a unidade de destino (atm, mmHg, cmHg, Pa, kPa): ").lower()

            if origem == 'atm' and destino == 'Pa':
                resultado = atmosfera_para_pascal(valor)

            elif origem == 'Pa' and destino == 'atm':
                resultado = pascal_para_atmosfera(valor)

            elif origem == 'atm' and destino == 'mmHg':
                resultado = atmosfera_para_mmHg(valor)

            elif origem == 'mmHg' and destino == 'atm':
                resultado = mmHg_para_atmosfera(valor)

            elif origem == 'atm' and destino == 'cmHg':
                resultado = atmosfera_para_cmHg(valor)

            elif origem == 'cmHg' and destino == 'atm':
                resultado = cmHg_para_atmosfera(valor)

            elif origem == 'Pa' and destino == 'kPa':
                resultado = pascal_para_quilopascal(valor)

            elif origem == 'kPa' and destino == 'Pa':
                resultado = quilopascal_para_pascal(valor)

            """else:
                print("Opção de conversão inválida.")"""

            print(f"{valor} {origem} = {resultado} {destino}")



        elif escolha == '5':  # Unidades de Comprimento
            valor = float(input("Digite o valor: "))
            origem = input("Digite a unidade de origem (km, m, cm, dm, mm): ").lower()
            destino = input("Digite a unidade de destino (km, m, cm, dm, mm): ").lower()

            if origem == 'km' and destino == 'm':
                resultado = quilometros_para_metros(valor)

            elif origem == 'm' and destino == 'km':
                resultado = metros_para_quilometros(valor)

            elif origem == 'm' and destino == 'cm':
                resultado = metros_para_centimetros(valor)

            elif origem == 'cm' and destino == 'm':
                resultado = centimetros_para_metros(valor)

            elif origem == 'm' and destino == 'dm':
                resultado = metros_para_decimetros(valor)

            elif origem == 'dm' and destino == 'm':
                resultado = decimetros_para_metros(valor)

            elif origem == 'm' and destino == 'mm':
                resultado = metros_para_milimetros(valor)

            elif origem == 'mm' and destino == 'm':
                resultado = milimetros_para_metros(valor)

            """else:
                print("Opção de conversão inválida.")"""

            print(f"{valor} {origem} = {resultado} {destino}")


        elif escolha == '6':  # Unidades de Energia
            valor = float(input("Digite o valor: "))
            origem = input("Digite a unidade de origem (J, kJ, cal, kcal): ").lower()
            destino = input("Digite a unidade de destino (J, kJ, cal, kcal): ").lower()

            if origem == 'J' and destino == 'cal':
                resultado = joule_para_caloria(valor)

            elif origem == 'cal' and destino == 'J':
                resultado = caloria_para_joule(valor)

            elif origem == 'kJ' and destino == 'J':
                resultado = quilojoule_para_joule(valor)

            elif origem == 'J' and destino == 'kJ':
                resultado = joule_para_quilojoule(valor)

            elif origem == 'kcal' and destino == 'cal':
                resultado = quilocaloria_para_caloria(valor)

            elif origem == 'cal' and destino == 'kcal':
                resultado = caloria_para_quilocaloria(valor)
            """else:
                print("Opção de conversão inválida.")"""

            print(f"{valor} {origem} = {resultado} {destino}")

        elif escolha == '7':  # Unidades de Tempo
            valor = float(input("Digite o valor: "))
            origem = input("Digite a unidade de origem (h, min, s): ").lower()
            destino = input("Digite a unidade de destino (h, min, s): ").lower()

            if origem == 'h' and destino == 'min':
                resultado = hora_para_minuto(valor)

            elif origem == 'min' and destino == 'h':
                resultado = minuto_para_hora(valor)

            elif origem == 'h' and destino == 's':
                resultado = hora_para_segundo(valor)

            elif origem == 's' and destino == 'h':
                resultado = segundo_para_hora(valor)

            elif origem == 'min' and destino == 's':
                resultado = minuto_para_segundo(valor)

            elif origem == 's' and destino == 'min':
                resultado = segundo_para_minuto(valor)

            """else:
                print("Opção de conversão inválida.")"""

            print(f"{valor} {origem} = {resultado} {destino}")

        elif escolha == '8':  # Unidades de Quantidade de Matéria
            valor = float(input("Digite o valor: "))
            origem = input("Digite a unidade de origem (Mol, quilomol): ").lower()
            destino = input("Digite a unidade de destino (Mol, quilomol): ").lower()

            if origem == 'mol' and destino == 'quilomol':
                resultado = mol_para_quilomol(valor)

            elif origem == 'quilomol' and destino == 'mol':
                resultado = quilomol_para_mol(valor)

            """else:
                print("Opção de conversão inválida.")"""

            print(f"{valor} {origem} = {resultado} {destino}")

        elif escolha == '9':  # Sair
            print("Obrigado por usar o Conversor de Unidades!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
