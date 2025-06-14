def format_product_code(product_id):
    """
    Format a product ID by inserting hyphens at specific positions.
    
    This function takes a product ID string and formats it by inserting
    hyphens after the 3rd and 6th characters.
    
    Parameters:
        product_id (str): A string of exactly 10 alphanumeric characters
    
    Returns:
        str: Formatted product code with hyphens (format: XXX-XXX-XXXX)
    
    Raises:
        ValueError: If product_id is not exactly 10 characters long or contains non-alphanumeric characters
    
    Examples:
        >>> format_product_code("ABC123DEF4")
        'ABC-123-DEF4'
        >>> format_product_code("XYZ987GHIJ")
        'XYZ-987-GHIJ'
        >>> format_product_code("SHORT")
        Raises ValueError: Product ID must be exactly 10 characters long, got 5
    """
    # Validate input is a string
    if not isinstance(product_id, str):
        raise ValueError(f"Product ID must be a string, got {type(product_id).__name__}")
    
    # Check length
    if len(product_id) != 10:
        raise ValueError(f"Product ID must be exactly 10 characters long, got {len(product_id)}")
    
    # Check if alphanumeric
    if not product_id.isalnum():
        raise ValueError("Product ID must contain only alphanumeric characters")
    
    # Format the product code
    formatted_code = f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"
    
    return formatted_code