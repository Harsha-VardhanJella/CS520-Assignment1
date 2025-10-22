def strlen(string: str) -> int:
    """
    Return the length of the given string.
    """
    count = 0
    for _ in string:
        count += 1
    return count
