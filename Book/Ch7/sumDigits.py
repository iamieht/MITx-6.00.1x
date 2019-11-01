def sumDigits(s):
    """ Assumes s is a string
        Returns the sum of the decimal digits in s
        For example, if s is 'a2b3c' it returns 5"""
    val = 0
    for element in s:
        try:
            val += int(element)
        except:
            pass
    return val

print(sumDigits('a2b3c'))