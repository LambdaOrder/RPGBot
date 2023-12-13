from random import randint
import math
def rolar(quantidade, lados):
    resultados = []
    for i in range(quantidade):
        resultado = randint(1, lados)
        resultados.append(resultado)
    return resultados

def proficiencia(atributo, bonus):
    """
    Esta função é utilizada para calcular prroficiencia em pericias e testes de resistencia

    atributo: nivel do atributo correspondente
    bonus: bonus de proficiencia do personagem


    >>> proficiencia(1,2)
    -3
    """
    pfc = math.floor((atributo - 10)/2)
    pfc += bonus
    return pfc
