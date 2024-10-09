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
    if re.search('V{2,}|L{2,}|D{2,}', s):
        return False
    if re.search('I{4,}|X{4,}|C{4,}|M{4,}', s):
        return False
    
    # Check for valid subtractive pairs
    valid_pairs = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    for pair in valid_pairs:
        if s.count(pair) > 1:
            return False
    
    # Check overall descending order
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = float('inf')
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in valid_pairs:
            current_value = values[s[i+1]] - values[s[i]]
            i += 2
        else:
            current_value = values[s[i]]
            i += 1
        if current_value > prev_value:
            return False
        prev_value = current_value
    
    return True

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
