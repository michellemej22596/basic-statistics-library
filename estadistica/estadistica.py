"""Funciones de estadística básica sobre listas de números."""


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
