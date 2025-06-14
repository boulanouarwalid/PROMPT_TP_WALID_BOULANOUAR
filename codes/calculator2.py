def calculate(a, b, op):
    """
    Perform a mathematical operation on two integers.
    
    Parameters:
        a (int): The first integer operand
        b (int): The second integer operand
        op (str): The operation to perform ('+', '-', '*', or '/')
    
    Returns:
        int or float: The result of the operation
            - Addition, subtraction, and multiplication return integers
            - Division returns a float rounded to 2 decimal places
    
    Raises:
        ValueError: If an invalid operation is provided
        ZeroDivisionError: If division by zero is attempted
    """
    # Validate input types
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both a and b must be integers")
    
    # Perform the requested operation
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        # Handle division by zero
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        # Round division result to 2 decimal places
        return round(a / b, 2)
    else:
        # Handle invalid operation
        raise ValueError(f"Invalid operation: {op}. Valid operations are '+', '-', '*', '/'")