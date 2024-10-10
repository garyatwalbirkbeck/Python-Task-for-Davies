import re

def is_valid_roman_numeral(s: str) -> bool:
    """
    Validate if the input string is a valid Roman numeral.
    
    Args:
        s (str): The input string to validate.
    
    Returns:
        bool: True if the input is a valid Roman numeral, False otherwise.
    """
    # Check for valid characters
    if not re.match('^[IVXLCDM]+$', s):
        return False
    
    # Check for invalid repetitions
    if re.search('I{4,}|X{4,}|C{4,}|M{4,}|V{2,}|L{2,}|D{2,}', s):
        return False
    
    # Define valid Roman numeral patterns
    """

    M{0,3}: Up to three M's at the beginning
    (CM|CD|D?C{0,3}): Either CM, CD, or up to three C's, optionally preceded by a D
    (XC|XL|L?X{0,3}): Either XC, XL, or up to three X's, optionally preceded by an L
    (IX|IV|V?I{0,3}): Either IX, IV, or up to three I's, optionally preceded by a V


    """
    valid_pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    
    return bool(re.match(valid_pattern, s))

def roman_to_int(roman_numeral: str) -> int:
    """
    Convert a Roman numeral to an integer.
    
    Args:
        roman_numeral (str): A string representing a Roman numeral.
    
    Returns:
        int: The integer value of the Roman numeral.
    
    Raises:
        ValueError: If the input is not a valid Roman numeral.
    """
    if not is_valid_roman_numeral(roman_numeral):
        raise ValueError(f"Invalid Roman numeral: {roman_numeral}")
    
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    result = 0
    prev_value = 0
    
    for char in reversed(roman_numeral.upper()):
        current_value = roman_values[char]
        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value
        
        prev_value = current_value
    
    return result

def int_to_roman(num: int) -> str:
    """
    Convert an integer to a Roman numeral.
    
    Args:
        num (int): An integer to convert (must be between 1 and 3999).
    
    Returns:
        str: The Roman numeral representation of the input integer.
    
    Raises:
        ValueError: If the input is not between 1 and 3999.
    """
    if not 1 <= num <= 3999:
        raise ValueError("Input must be between 1 and 3999")
    
    roman_symbols = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]
    
    result = []
    for symbol, value in roman_symbols:
        while num >= value:
            result.append(symbol)
            num -= value
    
    return ''.join(result)
