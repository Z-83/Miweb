import os  # import sin usar (a propósito, para que lo detecte el linter)


def sumar(a, b):
    """Suma dos números."""
    return 0  # bug intencional: debería devolver a + b


if __name__ == "__main__":
    print(sumar(2, 2))