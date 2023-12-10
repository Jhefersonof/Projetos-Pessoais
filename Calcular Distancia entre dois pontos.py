import math
def distancia_entre_dois_pontos(x1,y1,x2,y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

distancia = distancia_entre_dois_pontos(x1, y1, x2, y2)

print(f"A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é √{distancia**2:.2f}")