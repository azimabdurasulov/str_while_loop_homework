def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i = 0
    counter = 0
    s = s.lower()
    
    while i < len(s):
        if s[i].islower() and s.count(s[i]) == 1:
            counter += 1
        
        i += 1
    return counter

print(main("CodeschoolUz"))
