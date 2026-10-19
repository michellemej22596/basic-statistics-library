# basic-statistics-library

Librería de estadística básica en Python, desarrollada para la **Sesión Práctica #7 – Continuous Integration** del curso CC3047 Administración y Mantenimiento de Sistemas.

El proyecto pone en práctica control de versiones con Git, pruebas unitarias con `pytest` e integración continua con GitHub Actions.

## Funciones

| Función | Descripción | Ejemplo |
|---|---|---|
| `media(numeros)` | Media aritmética: suma de los valores entre la cantidad. | `media([1, 2, 3, 4, 5])` → `3.0` |
| `mediana(numeros)` | Valor central de la lista ordenada. Si la cantidad es par, promedia los dos centrales. | `mediana([4, 1, 3, 2])` → `2.5` |
| `moda(numeros)` | Valor que más se repite. Si hay empate, retorna el menor. | `moda([5, 3, 5, 3, 9])` → `3` |
| `variance(numeros)` | Varianza poblacional: promedio de las distancias al cuadrado a la media. | `variance([2, 4, 4, 4, 5, 5, 7, 9])` → `4.0` |
| `ds(numeros)` | Desviación estándar poblacional: raíz cuadrada de la varianza. | `ds([2, 4, 4, 4, 5, 5, 7, 9])` → `2.0` |

### Manejo de errores

Todas las funciones validan la entrada antes de calcular y lanzan una excepción en lugar de retornar un valor incorrecto:

| Entrada | Excepción |
|---|---|
| Lista vacía `[]` | `ValueError` |
| Algo que no es lista ni tupla (`None`, `"123"`) | `TypeError` |
| Lista con valores no numéricos (`[1, "a", 3]`) | `TypeError` |
| Lista con booleanos (`[1, True, 3]`) | `TypeError` |

## Estructura

```
basic-statistics-library/
├── estadistica/
│   ├── __init__.py          # Exporta las funciones públicas
│   └── estadistica.py       # Implementación y validación
├── tests/
│   └── test_estadistica.py  # Pruebas unitarias
├── .github/workflows/
│   └── tests.yml            # Workflow de GitHub Actions
├── pytest.ini
└── requirements.txt
```

## Uso

```python
from estadistica import media, mediana, moda, variance, ds

datos = [2, 4, 4, 4, 5, 5, 7, 9]
print(media(datos))     # 5.0
print(mediana(datos))   # 4.5
print(moda(datos))      # 4
print(variance(datos))  # 4.0
print(ds(datos))        # 2.0
```

## Ejecutar las pruebas

Requiere Python 3.9 o superior.

```bash
pip install -r requirements.txt
pytest -v
```

Cada función tiene al menos dos pruebas de casos exitosos y pasa por los cinco casos de error compartidos de la tabla anterior.

## Integración continua

El workflow `.github/workflows/tests.yml` ejecuta `pytest` en cada Pull Request hacia `main` (y en cada push a `main`).

La rama `main` está protegida: un Pull Request solo puede hacer merge si el check de pruebas pasa y tiene una aprobación.

## Flujo de trabajo

1. Crear una rama desde `main` actualizado (`feat/<funcion>`).
2. Implementar la función y sus pruebas; verificar localmente con `pytest -v`.
3. Hacer commit, push y abrir un Pull Request hacia `main`.
4. Esperar a que GitHub Actions apruebe el check y a la revisión de la pareja.
5. Hacer merge.
