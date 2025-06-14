def calculate(a, b, op):
    """
    Calculate the result of a mathematical operation between two integers.
    
    This function performs basic arithmetic operations (addition, subtraction,
    multiplication, division) on two integer values based on the provided operator.
    
    Parameters
    ----------
    a : int
        First integer operand
    b : int
        Second integer operand
    op : str
        Operation to perform ('+', '-', '*', or '/')
    
    Returns
    -------
    int or float
        Result of the operation. Division results are rounded to 2 decimal places.
    
    Raises
    ------
    TypeError
        If a or b are not integers
    ValueError
        If op is not one of the supported operations
    ZeroDivisionError
        If division by zero is attempted
    
    Examples
    --------
    >>> calculate(5, 3, '+')
    8
    >>> calculate(5, 3, '-')
    2
    >>> calculate(5, 3, '*')
    15
    >>> calculate(5, 3, '/')
    1.67
    """
    # Input validation
    if not isinstance(a, int):
        raise TypeError(f"First operand must be an integer, got {type(a).__name__}")
    
    if not isinstance(b, int):
        raise TypeError(f"Second operand must be an integer, got {type(b).__name__}")
    
    if not isinstance(op, str):
        raise TypeError(f"Operator must be a string, got {type(op).__name__}")
    
    # Dictionary mapping operators to lambda functions
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: round(x / y, 2) if y != 0 else None
    }
    
    # Check if the operator is valid
    if op not in operations:
        valid_ops = "', '".join(operations.keys())
        raise ValueError(f"Invalid operator '{op}'. Valid operators are: '{valid_ops}'")
    
    # Handle division by zero
    if op == '/' and b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    
    # Perform the operation
    return operations[op](a, b)