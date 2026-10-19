import math

import pytest

from estadistica import ds, media, mediana, moda, variance

# Entradas inválidas que todas las funciones deben rechazar con una excepción.
FUNCIONES = [media, mediana, moda, variance, ds]
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


# ---------- mediana ----------

def test_mediana_cantidad_impar():
    assert mediana([3, 1, 2]) == 2


def test_mediana_cantidad_par():
    assert mediana([4, 1, 3, 2]) == 2.5


def test_mediana_desordenada_con_negativos():
    assert mediana([10, -5, 0, 7, -1]) == 0


# ---------- moda ----------

def test_moda_un_valor_repetido():
    assert moda([1, 2, 2, 3]) == 2


def test_moda_decimales():
    assert moda([1.5, 2.5, 1.5, 4.0]) == 1.5


def test_moda_empate_retorna_el_menor():
    assert moda([5, 3, 5, 3, 9]) == 3


# ---------- variance ----------

def test_variance_enteros():
    assert variance([2, 4, 4, 4, 5, 5, 7, 9]) == 4


def test_variance_decimales():
    assert variance([1.5, 2.5, 3.5]) == pytest.approx(2 / 3)


def test_variance_valores_iguales_es_cero():
    assert variance([3, 3, 3]) == 0


# ---------- ds ----------

def test_ds_enteros():
    assert ds([2, 4, 4, 4, 5, 5, 7, 9]) == 2


def test_ds_decimales():
    assert ds([1.5, 2.5, 3.5]) == pytest.approx(math.sqrt(2 / 3))


def test_ds_valores_iguales_es_cero():
    assert ds([8, 8, 8]) == 0
