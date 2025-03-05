def factorial(n):
    if not isinstance(n, int):
        raise TypeError("El número debe ser un entero")
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    if n in [0, 1]:
        return 1
    return n * factorial(n - 1)