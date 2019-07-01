def square(n):
    """return square of the number"""
    return n*n


def cube(n):
    """return cube of the number"""
    return n*n*n


def triangle(n):
    """return triangle of the number"""
    sum = 0
    for i in range(n, 0, -1):
        sum = sum + i
    return sum

