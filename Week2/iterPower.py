# Write an iterative function iterPower(base, exp) that calculates the exponential baseexp by simply using successive multiplication. 
# For example, iterPower(base, exp) should compute baseexp by multiplying base times itself exp times. Write such a function below.

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1

    while exp > 0:
        result *= base
        exp -= 1
    
    return result

print(iterPower(2, 3))