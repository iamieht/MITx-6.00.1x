def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
#    testChar = aStr[len(aStr) // 2]

    if len(aStr) == 0:
        return False

    testChar = aStr[len(aStr) // 2]

    if len(aStr) == 1:
        return char == aStr
    elif testChar == char:
        return True
    else:
        if testChar > char:
            return isIn(char, aStr[:len(aStr)//2])
        else:
            return isIn(char, aStr[len(aStr)//2:])


print(isIn('b', 'ivan'))
    