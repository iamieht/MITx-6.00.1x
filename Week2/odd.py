# Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise. 

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return x % 2 != 0

print(odd(2))

