import pytest
from src.factorial import factorial

@pytest.mark.xfail(reason="Este test debe fallar intencionalmente")
def test_factorial_1_falla():
    assert factorial(1) == 2  # Esto debe fallar

@pytest.mark.xfail(reason="Este test debe fallar intencionalmente")
def test_factorial_1_falla():
    assert factorial(1) == 2  # Falla

def test_factorial_1_pasa():
    assert factorial(1) == 1  # Pasa

def test_tipo_falla():
    with pytest.raises(TypeError):
        factorial("texto")  # Falla

def test_tipo_pasa():
    with pytest.raises(TypeError):
        factorial(3.5)  # Pasa

def test_negativo_falla():
    with pytest.raises(ValueError):
        factorial(-5)  # Falla

def test_negativo_pasa():
    with pytest.raises(ValueError):
        factorial(-1)  # Pasa

def test_positivo_falla():
    assert factorial(5) == 200  # Falla

def test_positivo_pasa():
    assert factorial(5) == 120  # Pasa
