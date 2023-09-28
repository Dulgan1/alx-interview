#!/usr/bin/python3
"""
Interview practice - the pascals triangle
Definition: a triangular array of numbers in which those at the ends of the
            rows are 1 and each of the others is the sum of the nearest two
            numbers in the row above (the apex, 1, being at the top).
def pascal_triangle(n) - the function prodices a list of lists of integers
                        of the pascals triangle with n depth.
"""

def pascal_triangle(n):
    """
    n is assumed to be any integer

    the function produces a list of lists of integers, sequentially
    representing the depth of the triangle from top
    of the pascals triangle with n depth.
    """
    if not n:
        return []
    elif n == 1:
        return [[1]]
    n -= 1
    triangle = [[1]]
    while n:
        end_flag = 0
        level = [1, 1]
        recent_level = triangle[-1]
        for i in range(len(recent_level)):
            if (recent_level[i] == 1 and end_flag) or len(recent_level) == 1:
                break
            end_flag = 1
            new_ = recent_level[i] + recent_level[i + 1] \
                    if len(recent_level) != 1 else 2
            level.insert(-1, new_)
                
        triangle.append(level)
        n -= 1
    return triangle

if __name__ == "__main__":
    from sys import argv
    """"""
    tri = pascal_triangle(int(argv[1]))
    print(tri)
    for i in tri:
        print(i)
