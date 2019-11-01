def bisect_search1(L, e):
    """
    Input: Array, Num or String -> Boolean
    produces true if element on the list, False otherwise
    """
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)