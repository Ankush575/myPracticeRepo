
"""
A simple calculator module to perform basic arithmetic operations.
"""


def add(a, b):
    """Returns the sum of a and b."""
    return a + b


def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b


def multiply(a, b):
    """Returns the product of a and b."""
    return a * b


def divide(a, b):
    """Returns the quotient of a divided by b. Raises an error if division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulus(a, b):
    """Returns the modulus (remainder) of a divided by b."""
    return a % b
