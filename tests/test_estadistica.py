import pytest

from estadistica import media

# Entradas inválidas que todas las funciones deben rechazar con una excepción.
FUNCIONES = [media]
CASOS_ERROR = [
    ([], ValueError),          # lista vacía
    (None, TypeError),         # no es lista
    ("123", TypeError),        # cadena en vez de lista
    ([1, "a", 3], TypeError),  # elemento no numérico
    ([1, True, 3], TypeError), # booleano disfrazado de número
]


@pytest.mark.parametrize("funcion", FUNCIONES)
@pytest.mark.parametrize("entrada, excepcion", CASOS_ERROR)
def test_entradas_invalidas(funcion, entrada, excepcion):
    with pytest.raises(excepcion):
        funcion(entrada)


# ---------- media ----------

def test_media_enteros():
    assert media([1, 2, 3, 4, 5]) == 3


def test_media_decimales_y_negativos():
    assert media([-2.5, 0, 2.5, 10]) == pytest.approx(2.5)


def test_media_un_elemento():
    assert media([7]) == 7
