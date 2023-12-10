traducao = {
    'hello': 'olá',
    'world': 'mundo',
    'apple': 'maçã',
    'banana': 'banana',
    'dog': 'cão',
    'cat': 'gato'
}

def traduzir(texto):
    palavras = texto.split()  # Divide o texto em palavras

    traduzido = []

    for palavra in palavras:
        if palavra.lower() in traducao:
            traduzido.append(traducao[palavra.lower()])
        else:
            traduzido.append(palavra)

    texto_traduzido = ' '.join(traduzido)

    return texto_traduzido


texto_original = input("Digite o texto a ser traduzido: ")

texto_traduzido = traduzir(texto_original)
print("Texto traduzido:", texto_traduzido)
