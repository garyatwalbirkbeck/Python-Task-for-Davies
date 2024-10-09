import re

def reverse_words(sentence: str) -> str:
    """
    Reverse each word in a string while maintaining punctuation and spacing.
    
    Args:
        sentence (str): A string containing words to be reversed.
    
    Returns:
        str: A new string with each word reversed, maintaining original punctuation and spacing.
    """
    def reverse_word(word):
        # Reverse only alphanumeric characters
        alphanumeric = re.sub(r'\W+', '', word)
        reversed_alphanumeric = alphanumeric[::-1]
        
        # Rebuild the word with original punctuation
        result = []
        alphanumeric_index = 0
        for char in word:
            if char.isalnum():
                result.append(reversed_alphanumeric[alphanumeric_index])
                alphanumeric_index += 1
            else:
                result.append(char)
        return ''.join(result)
    
    # Split the sentence into words, preserving spacing
    words = re.split(r'(\s+)', sentence)
    
    # Reverse each word and join them back together
    return ''.join(reverse_word(word) for word in words)