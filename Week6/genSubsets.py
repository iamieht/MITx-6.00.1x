def genSubsets(L):
    """
    Input: Array -> Array
    produces a new Array with a subset of the elements in L
    """
    res = []
    if len(L) == 0:
        return [[]] # list of empty lists
    smaller = genSubsets(L[:-1]) # all subsets without the last element
    extra = L[-1:] # creates a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra)
    
    return smaller+new

#Test
print(genSubsets([0,1,2,3]))