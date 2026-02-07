def reverse_string(text):
    """
    Reverses a given string.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
    """
    return text[::-1]


if __name__ == "__main__":
    # Example usage
    sample = "Hello, World!"
    reversed_text = reverse_string(sample)
    print(f"Original: {sample}")
    print(f"Reversed: {reversed_text}")
