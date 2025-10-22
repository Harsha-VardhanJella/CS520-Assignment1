def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)