def reverse_words(sentence: str) -> str:
    """
    Reverse each word in a string.
    
    Args:
        sentence (str): A string containing words to be reversed.
    
    Returns:
        str: A new string with each word reversed.
    """
    return ' '.join(word[::-1] for word in sentence.split())