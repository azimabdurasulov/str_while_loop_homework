def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """ 
    i = 0
    counter = 0
    while i < len(s):
        counter += int(s[i])
        i += 1
    return counter

print(main("3245"))