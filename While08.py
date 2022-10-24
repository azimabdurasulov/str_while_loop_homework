def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    counter = 0

    while i < len(s):
        if int(s[i]) % 2 == 1:
            counter += 1
        i += 1
    return counter

print(main("12345678"))