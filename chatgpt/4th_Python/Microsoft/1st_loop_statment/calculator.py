def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b

def divide(a: float, b: float) -> float:
    """Return a divided by b. Raise ValueError if b is zero."""
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b
