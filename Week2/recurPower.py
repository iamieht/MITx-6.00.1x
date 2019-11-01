# Write a function recurPower(base, exp) which computes baseexp by recursively calling itself to solve a smaller version of the same problem, 
# and then multiplying the result by base to solve the initial problem. 

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)

print(recurPower(2, 3))