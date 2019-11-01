def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    returns a List
    '''
    result = []
    for key, value in aDict.items():
        if value == target:
            result.append(key)
    
    return sorted(result)

    

aDict = {1:1, 2:2, 3:3, 4:4, 5:2, 23:2, 15:2}
print(keysWithValue(aDict, 0))