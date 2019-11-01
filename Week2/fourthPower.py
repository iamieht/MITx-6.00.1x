# Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power. 
import square

def fourthPower(x):
    '''
    x: int or float.
    '''
    return square.square(square.square(x))

print(fourthPower(2))