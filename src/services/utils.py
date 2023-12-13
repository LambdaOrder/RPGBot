from random import randint
import math
def rolar(quantidade, lados):
    resultados = []
    for i in range(quantidade):
        resultado = randint(1, lados)
        resultados.append(resultado)
    return resultados

