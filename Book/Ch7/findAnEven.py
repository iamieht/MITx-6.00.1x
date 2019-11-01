def findAnEven(L):
    """ Assumes L is a list of integers
        Returns the first even number in L
        Raises ValueError if L does not contains an even number"""
    
    for item in L:
        if item%2 == 0:
            return item

    raise ValueError('List does not contain an even number')
            


print(findAnEven([1,1,1,3]))