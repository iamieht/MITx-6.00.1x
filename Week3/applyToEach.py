def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

def absolute(a):
    return abs(a)

applyToEach(testList, absolute)

def plusOne(a):
    return a + 1

applyToEach(testList, plusOne)

def square(a):
    return a**2

applyToEach(testList, square)