"""
Este módulo contiene la implementación de la función factorial.
"""

def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.

    Args:
        n (int): Un número entero no negativo.

    Returns:
        int: El factorial de n.

    Raises:
        TypeError: Si n no es un entero.
        ValueError: Si n es negativo.
    """
    
    if not isinstance(n, int):
        raise TypeError("El número debe ser un entero")
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    if n in [0, 1]:
        return 1
    return n * factorial(n - 1)
