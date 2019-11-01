def count7(N):
    '''
    N: a non-negative integer
    '''
    if N == 0:
        return 0
    elif N%10 == 7:
        return 1 + count7(N//10)
    else:
        return count7(N//10)

print(count7(717))
print(count7(1237123))
print(count7(8989))
