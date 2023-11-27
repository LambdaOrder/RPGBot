from random import randint
def rolar(quantidade, lados):
    resultados = []
    for i in range(quantidade):
        resultado = randint(1, lados)
        resultados.append(resultado)
    return resultados
