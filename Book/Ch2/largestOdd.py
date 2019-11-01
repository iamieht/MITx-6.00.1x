# Program that examines 3 variables and prints the largest odd number among them.

def largestOdd(x, y, z):
    odds = []
    for each in x,y,z:
        if each % 2 != 0:
            odds.append(each)
    
    return max(odds)



print(largestOdd(21, 1, 3))
        