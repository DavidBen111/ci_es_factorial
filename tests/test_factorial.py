import pytest
from src.factorial import factorial

@pytest.mark.xfail(reason="Este test debe fallar intencionalmente")
def test_factorial_1_falla():
    assert factorial(1) == 2  # Esto debe fallar

@pytest.mark.xfail(reason="Este test debe fallar intencionalmente")
def test_positivo_falla():
    assert factorial(5) == 200  # Debe fallar porque 5! = 120

def test_factorial_0():
    assert factorial(0) == 1

def test_factorial_1():
    assert factorial(1) == 1

def test_factorial_5():
    assert factorial(5) == 120

def test_factorial_10():
    assert factorial(10) == 3628800

def test_factorial_tipo():
    with pytest.raises(TypeError):
        factorial("string")

def test_factorial_negativo():
    with pytest.raises(ValueError):
        factorial(-1)