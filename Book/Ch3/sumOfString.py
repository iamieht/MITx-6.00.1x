# Ch3 - Finger Exercise 2
# Let s be a string that contains a sequence of decimal numbers separated by commas, e.r, s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s

def sumOfString(s):
    list_of_numbers = s.split(',')
    total = 0
    for number in list_of_numbers:
        total += float(number)
    return total

print(sumOfString('1.23,2.4,3.123'))
