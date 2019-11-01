# Function that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise.

def isIn(s1, s2):
    return s1 in s2 or s2 in s1

print(isIn('ivan', 'i'))