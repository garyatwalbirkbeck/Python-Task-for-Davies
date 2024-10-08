def roman_to_int(roman_numeral: str) -> int:
    """
    Convert a Roman numeral to an integer.
    
    Args:
        roman_numeral (str): A string representing a Roman numeral.
    
    Returns:
        int: The integer value of the Roman numeral.
    
    Raises:
        ValueError: If the input contains invalid Roman numeral characters.
    """
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    result = 0
    prev_value = 0
    
    for char in reversed(roman_numeral.upper()):
        if char not in roman_values:
            raise ValueError(f"Invalid Roman numeral character: {char}")
        
        current_value = roman_values[char]
        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value
        
        prev_value = current_value
    
    return result