"""Funciones de estadística básica sobre listas de números."""

import math


def _validar(numeros):
    """Verifica que `numeros` sea una lista o tupla no vacía de números.

    Lanza TypeError si no es lista/tupla o si contiene algo que no sea
    int/float (los booleanos se rechazan aunque Python los trate como int).
    Lanza ValueError si está vacía.
    """
    if not isinstance(numeros, (list, tuple)):
        raise TypeError("Se esperaba una lista o tupla de números")
    if len(numeros) == 0:
        raise ValueError("La lista no puede estar vacía")
    for n in numeros:
        if isinstance(n, bool) or not isinstance(n, (int, float)):
            raise TypeError(f"Valor no numérico en la lista: {n!r}")


def media(numeros):
    """Retorna la media aritmética: suma de los valores entre la cantidad."""
    _validar(numeros)
    return sum(numeros) / len(numeros)



def mediana(numeros):
    """Retorna el valor central de la lista ordenada.

    Si la cantidad de elementos es par, retorna el promedio de los dos centrales.
    """
    _validar(numeros)
    ordenados = sorted(numeros)
    n = len(ordenados)
    mitad = n // 2
    if n % 2 == 1:
        return ordenados[mitad]
    return ordenados[mitad]



def moda(numeros):
    """Retorna el valor que más se repite.

    Si hay empate entre varios valores, retorna el menor de ellos.
    """
    _validar(numeros)
    conteo = {}
    for n in numeros:
        conteo[n] = conteo.get(n, 0) + 1
    maximo = max(conteo.values())
    return min(valor for valor, veces in conteo.items() if veces == maximo)


def variance(numeros):
    """Retorna la varianza poblacional: promedio de las distancias al cuadrado a la media."""
    _validar(numeros)
    m = media(numeros)
    return sum((n - m) ** 2 for n in numeros) / len(numeros)


def ds(numeros):
    """Retorna la desviación estándar poblacional: raíz cuadrada de la varianza."""
    return math.sqrt(variance(numeros))
