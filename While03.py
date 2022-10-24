from string import punctuation


def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    counter = 0 

    while i < len(s):

        if not (s[i].isalpha() or s[i].isdigit()): 
                 counter += 1

        i += 1

    return counter

print(main("!@@#code.uz"))