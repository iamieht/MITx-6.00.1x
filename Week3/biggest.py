def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    count = 0
    biggest = 0
    for key in aDict.keys():
        count = len(aDict[key])
        if count > biggest:
            biggest = count
            biggest_key = key


    return biggest_key

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))