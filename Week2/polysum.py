def polysum(n, s):
    '''
    n: number of sides of the polygon
    s: length of each side
    returns the sum of the area and square of the perimeter of a regular polygon
    '''
    import math
    areaOfPolygon = 0.25 * n * s**2 / math.tan(math.pi / n)
    perimeterOfPolygon = (n * s) **2

    return round(areaOfPolygon + perimeterOfPolygon, 4)


