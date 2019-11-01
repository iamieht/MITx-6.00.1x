def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    result = ''
    answer = 0
    for cha in s:
        if cha in '0123456789':
            result += cha

    if result == '':
        raise ValueError
    else:
        for digit in result:
            answer += int(digit)

    return answer
            





#Test
print(sum_digits("a;35d4"))
print(sum_digits("a;d"))